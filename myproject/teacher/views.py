from django.shortcuts import render
import pandas as pd
import json
from teacher.models import StudentRecord

def choose_semester(request):
    return render(request,'teacher/choose_semester.html')

def one_semester(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        try:
            df = pd.read_excel(excel_file)

            required_cols = ['Name', 'Roll_No', 'Attendance']
            missing_cols = [col for col in required_cols if col not in df.columns]
            if missing_cols:
                return render(request, 'teacher/one_semester.html', {
                    'error': f"Missing required column(s): {', '.join(missing_cols)}"
                })

            subject_cols = [col for col in df.columns if col not in required_cols]
            if not subject_cols:
                return render(request, 'teacher/one_semester.html', {
                    'error': "No subject columns found."
                })

            # Ensure marks and attendance are numeric
            for col in subject_cols + ['Attendance']:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            if df[subject_cols + ['Attendance']].isnull().any().any():
                return render(request, 'teacher/one_semester.html', {
                    'error': "All marks and attendance values must be numeric."
                })

            # Convert to long format (one row per student per subject)
            df_long = df.melt(
                id_vars=['Name', 'Roll_No', 'Attendance'],
                value_vars=subject_cols,
                var_name='Subject',
                value_name='Marks'
            )

            # Aggregate per student
            student_perf = df_long.groupby(['Name', 'Roll_No', 'Attendance'], as_index=False)['Marks'].sum()

            # Sort by Marks descending (Top students first)
            student_perf = student_perf.sort_values(by='Marks', ascending=False)

            # DELETE old teacher data (optional)
            StudentRecord.objects.filter(user=request.user).delete()

            # SAVE TO DATABASE
            for _, row in df_long.iterrows():
                StudentRecord.objects.create(
                    user=request.user,
                    name=row['Name'],
                    roll_no=row['Roll_No'],
                    subject=row['Subject'],
                    marks=row['Marks'],
                    attendance=row['Attendance'],
                    semester=1   # since this is one semester
                    )

            # Serialize to JSON for template
            context = {
                'df_long': json.dumps(df_long.to_dict(orient='records')),       
                'student_perf': json.dumps(student_perf.to_dict(orient='records')),
            }

            return render(request, 'teacher/one_semester_analysis.html', context)

        except Exception as e:
            return render(request, 'teacher/one_semester.html', {
                'error': f"Error: {str(e)}"
            })

    return render(request, 'teacher/one_semester.html')

def multi_semester(request):
    """
    Uploads an Excel file containing multiple semesters' student data
    and renders the multi-semester performance analysis dashboard.
    """
    message = ""
    error = ""
    df_long_json = None  # Combined data for JS

    if request.method == "POST" and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        try:
            # Read Excel
            df = pd.read_excel(excel_file)

            if df.empty:
                return render(request, 'teacher/multi_semester.html', {'error': "Uploaded Excel file is empty."})

            # Required columns
            required_cols = ['Name', 'Roll_No', 'Semester', 'Attendance']
            missing_cols = [col for col in required_cols if col not in df.columns]
            if missing_cols:
                return render(request, 'teacher/multi_semester.html', {'error': f"Missing required columns: {', '.join(missing_cols)}"})

            # Subject columns
            subject_cols = [col for col in df.columns if col not in required_cols]
            if not subject_cols:
                return render(request, 'teacher/multi_semester.html', {'error': "No subject columns found."})

            # Ensure numeric values for marks and attendance
            for col in subject_cols + ['Attendance']:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            if df[subject_cols + ['Attendance']].isnull().any().any():
                return render(request, 'teacher/multi_semester.html', {'error': "All marks and attendance values must be numeric."})

            # Convert to long format for JS
            df_long = pd.melt(
                df,
                id_vars=required_cols,
                value_vars=subject_cols,
                var_name='Subject',
                value_name='Marks'
            )

            # DELETE old data of same user
            StudentRecord.objects.filter(user=request.user).delete()

            # SAVE TO DATABASE
            for _, row in df_long.iterrows():
                StudentRecord.objects.create(
                    user=request.user,
                    name=row['Name'],
                    roll_no=row['Roll_No'],
                    subject=row['Subject'],
                    marks=row['Marks'],
                    attendance=row['Attendance'],
                    semester=row['Semester']
                )

            # Convert to JSON for JS
            df_long_json = json.dumps(df_long.to_dict(orient='records'))

            # Identify semesters
            semesters = sorted(df['Semester'].unique())
            active_semester = semesters[0] if semesters else None

            message = "File uploaded and processed successfully!"

            context = {
                'message': message,
                'error': error,
                'df_long': df_long_json,
                'semesters': semesters,
                'active_semester': active_semester
            }

            # Render analysis page
            return render(request, 'teacher/multi_semester_analysis.html', context)

        except Exception as e:
            return render(request, 'teacher/multi_semester.html', {'error': f"Error processing file: {str(e)}"})

    # GET request -> render upload page
    return render(request, 'teacher/multi_semester.html', {'message': message, 'error': error})