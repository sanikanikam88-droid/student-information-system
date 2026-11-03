from IPython.display import display, HTML

students = [
    {"name": "Sanika Nikam", "roll": 101, "course": "BCA"},
    {"name": "Priya Sharma", "roll": 102, "course": "BCA"},
    {"name": "Rahul Patil", "roll": 103, "course": "BCA"},
    {"name": "Amit Joshi", "roll": 104, "course": "BCA"},
    {"name": "Sneha More", "roll": 105, "course": "BCA"}
]

html = """
<h1 style="text-align:center;color:#2457a7;">
    Student Information System
</h1>
<h3 style="text-align:center;">Registered Student List</h3>
<table style="width:100%;border-collapse:collapse;text-align:center;">
<tr style="background:#2457a7;color:white;">
<th style="padding:12px;">Roll No.</th>
<th>Name</th>
<th>Course</th>
</tr>
"""

for student in students:
    html += f"""
    <tr>
    <td style="padding:12px;border-bottom:1px solid #ddd;">
    {student['roll']}</td>
    <td style="border-bottom:1px solid #ddd;">
    {student['name']}</td>
    <td style="border-bottom:1px solid #ddd;">
    {student['course']}</td>
    </tr>
    """

html += "</table>"

display(HTML(html))
