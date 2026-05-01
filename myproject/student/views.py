from django.shortcuts import render
import pandas as pd
import json
from teacher.models import StudentRecord

def student_upload(request):
    if request.method == "POST" and request.FILES.get('student_file'):
        file = request.FILES['student_file']

        try:
            # Handle both CSV and Excel
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)

            # Check empty file
            if df.empty:
                return render(request, 'student/upload.html', {
                    'error': "Uploaded file is empty."
                })

            # Required columns
            required_cols = ['Semester', 'Subject', 'Marks', 'Attendance']
            missing_cols = [col for col in required_cols if col not in df.columns]

            if missing_cols:
                return render(request, 'student/upload.html', {
                    'error': f"Missing columns: {', '.join(missing_cols)}"
                })

            # Convert to numeric
            df['Marks'] = pd.to_numeric(df['Marks'], errors='coerce')
            df['Attendance'] = pd.to_numeric(df['Attendance'], errors='coerce')

            if df[['Marks', 'Attendance']].isnull().any().any():
                return render(request, 'student/upload.html', {
                    'error': "Marks and Attendance must be numeric."
                })
            
            # DELETE OLD DATA
            StudentRecord.objects.filter(
                user=request.user,
                semester__in=df['Semester'].unique()
                ).delete()
            # SAVE DATA TO DATABASE
            for _, row in df.iterrows():
                StudentRecord.objects.create(
                    user=request.user,
                    name=request.user.username,   # student name
                    roll_no=0,                    # you can improve later
                    subject=row['Subject'],
                    marks=row['Marks'],
                    attendance=row['Attendance'],
                    semester=row['Semester']
                )
            # Convert to JSON
            df_json = json.dumps(df.to_dict(orient='records'))

            # Render ANALYSIS page (IMPORTANT)
            return render(request, 'student/student_analysis.html', {
                'df_long': df_json
            })

        except Exception as e:
            return render(request, 'student/upload.html', {
                'error': f"Error: {str(e)}"
            })

    # GET request → show upload page
    return render(request, 'student/upload.html')