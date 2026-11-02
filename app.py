from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key' # Flash messages ke liye zaroori hai

# Aapka Resume Data
RESUME = {
    "name": "Akash Kumar Paswan",
    "title": "Electronic Engineer | Robotics | Programmer | AI/ML | QA",
    "email": "Akashpassi99@gmail.com",
    "phone": "+91 8755954409",
    "location": "R.K. Puram, Tarlaadhoiwala, Dehradun",
    "about": "Hello, I'm Akash, an electronic engineer passionate about creating innovative solutions. Skilled in Robotics, Embedded Systems, programming, circuit design etc, I enjoy designing electronic systems that solve real-world problems. I am committed to keeping up with the newest technology trends and am excited to use my skills on important projects.",
    "education": [
        {"degree": "Diploma in Electronic Engineering", "institute": "Govt. Polytechnic Dehradun", "year": ""},
        {"degree": "Electrician Trade", "institute": "Mahadev Pvt. ITI, Haridwar", "year": ""},
        {"degree": "High School (CBSE)", "institute": "Shri Guru Ram Rai Public School, Dehradun", "year": ""}
    ],
    "skills": {
        "Electronics & Hardware": "Analog & Digital Circuits, PCB Design, Embedded Systems, IoT, Robotics, Sensor Interfacing, Microcontrollers (ESP32, ATmega328P, etc.)",
        "Programming & Automation": "Python, C Programming, Machine Learning, AI (CNN, Defect Detection), Data Analysis",
        "Quality Engineering": "RCA, 7 QC Tools, 8D Methodology, PFMEA, Control Plan, PDCA, 5S, Kaizen",
        "Leadership": "Manpower Planning, Team Handling, Operator Training, Cross-Functional Coordination"
    },
    "experience": [
        {
            "role": "Asst. Team Leader - Quality Assurance",
            "company": "ATL Battery Technology Pvt. Ltd., Bawal",
            "duration": "Aug 2024 - Present",
            "points": [
            "Manage daily manpower planning, assign tasks to operators, and ensure smooth operation across all production lines.",
            "Manage shifts according to production plans to achieve daily production targets.",
            "Conduct CFT alignment and coordinate with concerned departments to resolve quality and process issues.",
            "Take immediate Block Action whenever defects or abnormalities are detected to prevent defective cells from moving further in the process.",
            "Handle customer audits at internal plants and ensure timely closure of identified issues.",
            "Train and guide operators to improve defect identification skills and ensure compliance with standard work procedures.",
            "Conduct daily line audits and inspections to verify compliance with SOPs and process parameters.",
            "Prepare Prime Yield defect reports and analysis charts to monitor trends and identify improvement areas.",
            "Conduct IPQC process audits to ensure compliance with SOPs, control plans, and quality standards.",
            "Perform machine audits to verify equipment conditions, calibration status, and process readiness.",
            "Verify critical process parameters through SPC, MES, and machine parameter monitoring to ensure product quality and process stability.",
            "Monitor SPC charts and investigate abnormal trends to prevent potential quality issues.",
            "Perform rework audits and verify reworked materials before releasing them for production.",
            "Support New Product Introduction (NPI) activities and ensure smooth transition from NPI to Mass Production (MP).",
            "Conduct First Article Inspection (FAI) and process validation during model changeovers.",
            "Verify instrument calibration status and conduct daily instrument spot checks.",
            "Conduct 5S audits and ensure compliance with workplace organization standards.",
            "Review MRB status, dynamic sampling, material hold/release, and segregation activities.",
            "Track NCRs and ODS issues and follow up with responsible departments for timely closure.",
            "Prepare daily quality reports, shift handover reports, and KPI monitoring reports.",
            "Coordinate with Production, ME, PE, and QA teams for root cause analysis and corrective actions.",
            "Participate in internal audits, risk management activities, and quality improvement projects."
            ]
        },
        {
            "role": "Self-Employed (Freelance Electronics Projects)",
            "company": "Freelance",
            "duration": "2022 - 2024",
            "points": [
                "Worked independently on electronics-based automation and robotics projects.",
                "Designed custom PCBs and troubleshooting electronic circuits.",
                "Assisted local clients in developing prototype systems using embedded platforms."
            ]
        }
    ]
}

# Aapke Projects (Resume ke anusar)
PROJECTS = [
    {
        "title": "AI Robotic Arm",
        "desc": "Developed an AI-powered robotic arm for precise object manipulation and recognition.",
        "tech": ["Python", "AI/ML", "Robotics", "Embedded"]
    },
    {
        "title": "3D Printer",
        "desc": "Designed and built a compact 3D printer with high print quality and speed for prototyping purposes.",
        "tech": ["Hardware", "3D Printing", "CAD"]
    },
    {
        "title": "IoT Home Automation",
        "desc": "Developed an IoT-based system to automate home devices for convenience and energy efficiency.",
        "tech": ["IoT", "ESP32/ESP8266", "C"]
    },
    {
        "title": "Bots (Line Follower, Obstacle Avoidance, Mobile Controlled)",
        "desc": "Engineered robots with smart sensors for autonomous navigation and versatile remote operation.",
        "tech": ["Robotics", "Sensors", "Microcontrollers"]
    },
    {
        "title": "EMPTX (Employee Performance & Attendance Tracking App)",
        "desc": "Developed an Android app for employee management, attendance tracking, and KPI-based performance monitoring.",
        "tech": ["Flutter", "Android", "Dart"]
    },
    {
        "title": "Smart QA Toolkit (Quality Analytics & Monitoring Web App)",
        "desc": "Developed a Python-based web application for manufacturing quality analysis, production monitoring, defect tracking, and shift-wise performance dashboards.",
        "tech": ["Python", "Streamlit", "Pandas", "Plotly", "Excel", "Data Analytics"]
    }

]

# Aapki App
# Aapki Apps
APPS = [
    {
        "name": "EMPTX (Employee Management & Performance Tracking App)", # Ya apni nayi app ka naam
        "desc": "Developed an Android and iOS app for employee management, attendance tracking, and KPI-based performance monitoring.",
        "tech": ["Flutter", "Android", "iOS", "Dart"],
        "apk_link": "/static/emptX.apk",       # Yahan apni APK file ka naam dalein
        "ios_link": "https://testflight.apple.com/..." # Yahan iOS ka link dalein
    },
    {
        "name": "Smart QA Toolkit (Quality Analytics & Monitoring Web App)",
        "desc": "Developed a Python-based web application for manufacturing quality analysis, production monitoring, defect tracking, and shift-wise performance dashboards.",
        "tech": ["Python", "Streamlit", "Pandas", "Plotly", "Excel", "Data Analytics"],
        "apk_link": "https://akash-toolkitatli.streamlit.app/",  # Web app hai toh APK nahi hai
        "ios_link": ""   # Web app hai toh iOS nahi hai
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS)

@app.route('/apps')
def apps():
    return render_template('apps.html', apps=APPS)

@app.route('/resume')
def resume():
    return render_template('resume.html', resume=RESUME)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Abhi ke liye hum bas message print karenge console mein
        print(f"New Message from {name} ({email}): {message}")
        flash("Thank you! Aapka message send ho gaya hai.", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)