from __future__ import annotations

from datetime import datetime
from typing import List, Dict
import secrets
import hashlib

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session

app = Flask(__name__)
app.secret_key = "dev-secret-change-me"

SCHOOL_NAME = "Behaira STEM School"

# Global STEM Programs Database (~40 programs)
GLOBAL_PROGRAMS: List[Dict] = [
    # TOP-TIER PROGRAMS
    {
        "id": 1,
        "name": "MIT MITES (Minority Introduction to Engineering and Science)",
        "organization": "Massachusetts Institute of Technology",
        "level": "Top-Tier",
        "type": "Summer School",
        "description": "Intensive 4-week summer program for talented minority high school students in STEM.",
        "full_description": "MITES is a highly selective summer program designed to introduce promising minority high school students to engineering and science. Participants engage in hands-on projects, research, and mentorship from MIT faculty.",
        "cost": "Paid",
        "aid": True,
        "duration": "4 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "January–March",
        "eligibility": "US minority students (African American, Latino, Native American)",
        "website": "https://mites.mit.edu",
        "why_matters": "Exposure to world-class research, networking with MIT students and faculty, and preparation for engineering careers."
    },
    {
        "id": 2,
        "name": "Ross Mathematics Program",
        "organization": "Ohio State University",
        "level": "Top-Tier",
        "type": "Summer School",
        "description": "Intensive pure mathematics program for exceptional high school students.",
        "full_description": "The Ross Program is an intensive summer program that introduces students to advanced mathematics, abstract algebra, and number theory through problem-solving and discovery.",
        "cost": "Paid",
        "aid": True,
        "duration": "6 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "December–January",
        "eligibility": "Strong mathematical ability; international students welcome",
        "website": "https://u.osu.edu/rossmath/",
        "why_matters": "Rigorous mathematics training and preparation for math competitions and careers in theoretical science."
    },
    {
        "id": 3,
        "name": "Harvard Summer School for High School Students",
        "organization": "Harvard University",
        "level": "Top-Tier",
        "type": "Summer School",
        "description": "Select STEM courses at Harvard for advanced high school students.",
        "full_description": "Harvard offers advanced STEM courses including organic chemistry, physics, computational biology, and advanced mathematics.",
        "cost": "Paid",
        "aid": False,
        "duration": "6–7 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "February–March",
        "eligibility": "GPA 3.7+, strong academics",
        "website": "https://www.summer.harvard.edu/high-school/",
        "why_matters": "College-level coursework, Harvard credential, networking with future leaders."
    },
    {
        "id": 4,
        "name": "Caltech STEM Outreach Program (CSOP)",
        "organization": "California Institute of Technology",
        "level": "Top-Tier",
        "type": "Summer School",
        "description": "Research-focused summer program for outstanding STEM students.",
        "full_description": "Caltech's STEM program offers hands-on research experience in physics, chemistry, biology, and engineering.",
        "cost": "Paid",
        "aid": True,
        "duration": "8 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "January–March",
        "eligibility": "Strong GPA, demonstrated STEM interest",
        "website": "https://www.caltech.edu",
        "why_matters": "World-class research experience at one of the top STEM institutions globally."
    },
    {
        "id": 5,
        "name": "International Science Olympiad (ISO)",
        "organization": "International Science Olympiad Organization",
        "level": "Top-Tier",
        "type": "Competition",
        "description": "Global competition in science disciplines with preparation programs.",
        "full_description": "Annual competition bringing together top science students from 100+ countries in biology, chemistry, physics, and earth science.",
        "cost": "Paid",
        "aid": False,
        "duration": "1 week (competition)",
        "location": "International",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Varies by country",
        "eligibility": "Selected through national competitions",
        "website": "https://www.soinc.org",
        "why_matters": "Global competition, international exposure, recognition of excellence in STEM."
    },
    # ACHIEVABLE PROGRAMS
    {
        "id": 6,
        "name": "Johns Hopkins Summer Programs",
        "organization": "Johns Hopkins University",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Diverse STEM courses and research opportunities for high school students.",
        "full_description": "Johns Hopkins offers engineering, pre-med, computer science, and biomedical research programs.",
        "cost": "Paid",
        "aid": True,
        "duration": "4–6 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "March–April",
        "eligibility": "GPA 3.5+, interest in STEM",
        "website": "https://www.jhu.edu/summer-programs/",
        "why_matters": "Strong university credential, research experience, pre-med preparation."
    },
    {
        "id": 7,
        "name": "University of Pennsylvania Pre-College Programs",
        "organization": "University of Pennsylvania",
        "level": "Achievable",
        "type": "Summer School",
        "description": "College-level STEM courses taught by Penn faculty.",
        "full_description": "Engineering, computer science, mathematics, and biology courses with college credit.",
        "cost": "Paid",
        "aid": True,
        "duration": "4–6 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "April–May",
        "eligibility": "Sophomore+, strong academics",
        "website": "https://www.penn.edu/pre-college",
        "why_matters": "College credit, exposure to Ivy League, potential admissions boost."
    },
    {
        "id": 8,
        "name": "Cornell Neuroscience Summer Research Program",
        "organization": "Cornell University",
        "level": "Achievable",
        "type": "Research",
        "description": "Hands-on neuroscience research mentorship for high school students.",
        "full_description": "Students conduct original research under faculty supervision in neurobiology and brain science.",
        "cost": "Free",
        "aid": False,
        "duration": "8 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "February–March",
        "eligibility": "Strong biology background, research interest",
        "website": "https://www.cornell.edu/research/",
        "why_matters": "Original research experience, publication potential, career exploration."
    },
    {
        "id": 9,
        "name": "UC Berkeley Physics Summer Camp",
        "organization": "University of California, Berkeley",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Intensive physics and modern physics exploration for high schoolers.",
        "full_description": "Covers quantum mechanics, particle physics, and experimental design.",
        "cost": "Paid",
        "aid": True,
        "duration": "4 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "March–April",
        "eligibility": "Physics background, GPA 3.5+",
        "website": "https://www.berkeley.edu/about/",
        "why_matters": "Top-tier physics education, exposure to cutting-edge research."
    },
    {
        "id": 10,
        "name": "Science Olympiad National Tournament",
        "organization": "Science Olympiad Organization",
        "level": "Achievable",
        "type": "Competition",
        "description": "National competition in 23 STEM events across biology, chemistry, physics, and engineering.",
        "full_description": "Teams of 15 compete in diverse STEM events from building bridges to forensics.",
        "cost": "Free",
        "aid": False,
        "duration": "1 day (nationals)",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Ongoing (regional qualifiers)",
        "eligibility": "Part of school Science Olympiad team",
        "website": "https://www.soinc.org",
        "why_matters": "National recognition, team collaboration, diverse STEM exploration."
    },
    {
        "id": 11,
        "name": "FIRST Robotics Competition (FRC)",
        "organization": "FIRST (For Inspiration and Recognition of Science and Technology)",
        "level": "Achievable",
        "type": "Innovation / Entrepreneurship",
        "description": "Team-based robotics engineering competition with real-world engineering challenges.",
        "full_description": "Teams design, build, and program robots to compete in annual challenges.",
        "cost": "Paid",
        "aid": True,
        "duration": "6 weeks (build season)",
        "location": "On-campus",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Ongoing",
        "eligibility": "School team membership",
        "website": "https://www.firstinspires.org/robotics/frc",
        "why_matters": "Real engineering practice, professional mentorship, career pathways."
    },
    {
        "id": 12,
        "name": "Regeneron ISEF (International Science and Engineering Fair)",
        "organization": "Intel and Regeneron",
        "level": "Achievable",
        "type": "Research",
        "description": "Largest international student research competition.",
        "full_description": "Students present independent or team research projects across 17 categories.",
        "cost": "Free",
        "aid": False,
        "duration": "3 days (finals)",
        "location": "On-campus",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Year-round (regional fairs)",
        "eligibility": "Research project required",
        "website": "https://www.ssef.org",
        "why_matters": "Global recognition, research experience, networking with peers worldwide."
    },
    {
        "id": 13,
        "name": "Stanford Pre-Collegiate Summer Institute (STEM Focus)",
        "organization": "Stanford University",
        "level": "Achievable",
        "type": "Summer School",
        "description": "College-level STEM courses and seminars at Stanford.",
        "full_description": "Engineering, computer science, chemistry, and biology courses.",
        "cost": "Paid",
        "aid": True,
        "duration": "3–4 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "April–May",
        "eligibility": "GPA 3.6+",
        "website": "https://summer.stanford.edu/programs/pre-collegiate",
        "why_matters": "Stanford experience, college credit, Silicon Valley proximity."
    },
    {
        "id": 14,
        "name": "HHMI Science Internship Program",
        "organization": "Howard Hughes Medical Institute",
        "level": "Achievable",
        "type": "Research",
        "description": "Paid summer biomedical research internships.",
        "full_description": "Students work in HHMI laboratories conducting original biological research.",
        "cost": "Free",
        "aid": False,
        "duration": "8–10 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "November–December",
        "eligibility": "Strong biology background, research interest",
        "website": "https://www.hhmi.org/news-events/news/internships",
        "why_matters": "World-class biomedical research, stipend included, publication potential."
    },
    # ACCESSIBLE PROGRAMS
    {
        "id": 15,
        "name": "Khan Academy STEM Courses",
        "organization": "Khan Academy",
        "level": "Accessible",
        "type": "Online / Hybrid",
        "description": "Free online STEM courses from beginner to advanced levels.",
        "full_description": "Self-paced learning in mathematics, physics, chemistry, biology, and computer science.",
        "cost": "Free",
        "aid": False,
        "duration": "Self-paced",
        "location": "Online",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Anytime",
        "eligibility": "Any student, any background",
        "website": "https://www.khanacademy.org",
        "why_matters": "Free, flexible learning at any pace, excellent quality content."
    },
    {
        "id": 16,
        "name": "Coursera for High School",
        "organization": "Coursera",
        "level": "Accessible",
        "type": "Online / Hybrid",
        "description": "University-level STEM courses online with financial aid available.",
        "full_description": "Courses from top universities in engineering, computer science, and data science.",
        "cost": "Free",
        "aid": False,
        "duration": "6–12 weeks per course",
        "location": "Online",
        "country": "Global",
        "grades": ["10", "11", "12"],
        "application_window": "Continuous enrollment",
        "eligibility": "Any student",
        "website": "https://www.coursera.org",
        "why_matters": "University-level content, low-cost, globally accessible, certificates available."
    },
    {
        "id": 17,
        "name": "Codecademy STEM Bootcamp",
        "organization": "Codecademy",
        "level": "Accessible",
        "type": "Online / Hybrid",
        "description": "Interactive coding and computer science courses.",
        "full_description": "Learn Python, JavaScript, web development, and data science through interactive projects.",
        "cost": "Free",
        "aid": False,
        "duration": "Self-paced (40+ hours)",
        "location": "Online",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Anytime",
        "eligibility": "Any student",
        "website": "https://www.codecademy.com",
        "why_matters": "Practical coding skills, job-ready qualifications, affordable access."
    },
    {
        "id": 18,
        "name": "National Math & Science Initiative (NMSI)",
        "organization": "National Math & Science Initiative",
        "level": "Accessible",
        "type": "Summer School",
        "description": "College test prep and STEM enrichment for underserved students.",
        "full_description": "Free or low-cost summer programs in math, science, and test preparation.",
        "cost": "Free",
        "aid": False,
        "duration": "4–8 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "April–May",
        "eligibility": "Underserved/underrepresented students",
        "website": "https://www.nms.org",
        "why_matters": "Equity-focused, free for eligible students, strong college prep."
    },
    {
        "id": 19,
        "name": "Google Summer of Code",
        "organization": "Google",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Paid internship program for open-source software development.",
        "full_description": "Work on real open-source projects with experienced mentors.",
        "cost": "Free",
        "aid": False,
        "duration": "12 weeks",
        "location": "Online",
        "country": "Global",
        "grades": ["11", "12"],
        "application_window": "November–January",
        "eligibility": "Coding experience, open-source interest",
        "website": "https://summerofcode.withgoogle.com",
        "why_matters": "Real-world coding experience, paid internship, portfolio building, Google recognition."
    },
    {
        "id": 20,
        "name": "FTC (FIRST Tech Challenge)",
        "organization": "FIRST",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Robotics team competition for younger students (7th–12th grade).",
        "full_description": "Teams design and program robots for annual engineering challenges.",
        "cost": "Paid",
        "aid": True,
        "duration": "8 weeks (season)",
        "location": "On-campus",
        "country": "Global",
        "grades": ["7", "8", "9", "10"],
        "application_window": "Ongoing",
        "eligibility": "School team",
        "website": "https://www.firstinspires.org/robotics/ftc",
        "why_matters": "Accessible robotics, younger student engagement, strong STEM foundation."
    },
    {
        "id": 21,
        "name": "TechCrunch Disrupt Startup Battlefield",
        "organization": "TechCrunch",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "High school startup competition and pitching event.",
        "full_description": "Pitch your startup idea to investors and tech industry leaders.",
        "cost": "Free",
        "aid": False,
        "duration": "2 days (main event)",
        "location": "On-campus",
        "country": "Global",
        "grades": ["10", "11", "12"],
        "application_window": "February–March",
        "eligibility": "Startup idea or company required",
        "website": "https://techcrunch.com/disrupt/",
        "why_matters": "Entrepreneurship exposure, investor connections, innovation showcase."
    },
    {
        "id": 22,
        "name": "Bridger Aerospace STEM Outreach",
        "organization": "Bridger Aerospace",
        "level": "Accessible",
        "type": "Summer School",
        "description": "Aerospace engineering workshops and mentorship.",
        "full_description": "Learn aircraft design, materials science, and aerospace engineering.",
        "cost": "Free",
        "aid": False,
        "duration": "2–4 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "May–June",
        "eligibility": "Interest in aerospace",
        "website": "https://www.bridgeraerospace.com",
        "why_matters": "Specialized STEM field, industry exposure, career pathways."
    },
    {
        "id": 23,
        "name": "Girls Who Code Summer Immersion Program",
        "organization": "Girls Who Code",
        "level": "Accessible",
        "type": "Summer School",
        "description": "Intensive 7-week coding and computer science program for high school girls.",
        "full_description": "Project-based learning in web development, mobile apps, and cybersecurity.",
        "cost": "Free",
        "aid": False,
        "duration": "7 weeks",
        "location": "On-campus / Online",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "January–February",
        "eligibility": "Female-identifying students",
        "website": "https://girlswhocode.com",
        "why_matters": "Equity-focused, community-driven, career preparation in tech."
    },
    {
        "id": 24,
        "name": "MIT Open CourseWare (OCW)",
        "organization": "Massachusetts Institute of Technology",
        "level": "Accessible",
        "type": "Online / Hybrid",
        "description": "Free MIT courses including advanced STEM subjects.",
        "full_description": "Full MIT courseware (lecture notes, exams, videos) from undergraduate and graduate courses.",
        "cost": "Free",
        "aid": False,
        "duration": "Self-paced",
        "location": "Online",
        "country": "Global",
        "grades": ["11", "12"],
        "application_window": "Anytime",
        "eligibility": "Any student",
        "website": "https://ocw.mit.edu",
        "why_matters": "World-class MIT content free, college-level rigor, self-directed learning."
    },
    {
        "id": 25,
        "name": "BioBuilder Online Community",
        "organization": "BioBuilder Educational Foundation",
        "level": "Accessible",
        "type": "Online / Hybrid",
        "description": "Free synthetic biology and biotechnology learning platform.",
        "full_description": "STEM curriculum with virtual labs and real-world biotechnology projects.",
        "cost": "Free",
        "aid": False,
        "duration": "Self-paced",
        "location": "Online",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Anytime",
        "eligibility": "Any student",
        "website": "https://www.biobuildereducation.org",
        "why_matters": "Biotechnology exposure, virtual labs, emerging field access."
    },
    {
        "id": 26,
        "name": "International Science Olympiad (Youth Division)",
        "organization": "International Science Olympiad",
        "level": "Accessible",
        "type": "Competition",
        "description": "Youth-focused science competition with regional qualifiers.",
        "full_description": "Less competitive than main ISO but still rigorous science events.",
        "cost": "Free",
        "aid": False,
        "duration": "1 day (regionals)",
        "location": "On-campus",
        "country": "Global",
        "grades": ["9", "10"],
        "application_window": "Throughout year",
        "eligibility": "Grades 9–10",
        "website": "https://www.soinc.org",
        "why_matters": "Entry to international competition, builds competition skills gradually."
    },
    {
        "id": 27,
        "name": "Project Lead The Way (PLTW)",
        "organization": "Project Lead The Way",
        "level": "Accessible",
        "type": "Online / Hybrid",
        "description": "Project-based engineering and computer science curriculum.",
        "full_description": "Available in many schools; covers Civil Engineering, Computer Science, Biomedical Engineering, etc.",
        "cost": "Free",
        "aid": False,
        "duration": "Semester / Year-long",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Ongoing enrollment",
        "eligibility": "Offered in school",
        "website": "https://www.pltw.org",
        "why_matters": "Industry-recognized, college-credit pathway, career-focused."
    },
    {
        "id": 28,
        "name": "DEF CON Hacking Conference (Teens)",
        "organization": "DEF CON",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Cybersecurity and ethical hacking conference with teen track.",
        "full_description": "Workshops in cybersecurity, CTF (Capture The Flag) competitions, and hands-on hacking.",
        "cost": "Paid",
        "aid": False,
        "duration": "3 days",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "May–June",
        "eligibility": "Any student interest",
        "website": "https://www.defcon.org",
        "why_matters": "Cybersecurity careers, ethical hacking education, cutting-edge tech."
    },
    {
        "id": 29,
        "name": "Youth Business Summit (NFTE)",
        "organization": "Network for Teaching Entrepreneurship",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Entrepreneurship training and business plan competition.",
        "full_description": "Teach students to start their own businesses with mentorship and seed funding.",
        "cost": "Free",
        "aid": False,
        "duration": "6 months – 1 year",
        "location": "On-campus",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Rolling",
        "eligibility": "Business idea or interest",
        "website": "https://www.nfte.com",
        "why_matters": "Real business skills, mentorship, potential funding for startups."
    },
    {
        "id": 30,
        "name": "NASA STEM Resources & Competitions",
        "organization": "National Aeronautics and Space Administration",
        "level": "Accessible",
        "type": "Competition",
        "description": "Various NASA competitions in robotics, design, and innovation.",
        "full_description": "NASA Lunabotics, Mars Rover Design Competition, and other STEM challenges.",
        "cost": "Free",
        "aid": False,
        "duration": "Varies (3 days – semester)",
        "location": "Online / On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Year-round",
        "eligibility": "Team-based, various requirements",
        "website": "https://www.nasa.gov/stem/",
        "why_matters": "Space exploration passion, government recognition, career exposure."
    },
    {
        "id": 31,
        "name": "American Chemical Society (ACS) National High School Chemistry Olympiad",
        "organization": "American Chemical Society",
        "level": "Accessible",
        "type": "Competition",
        "description": "National chemistry competition for high school students.",
        "full_description": "Rigorous chemistry knowledge test with state and national competition rounds.",
        "cost": "Free",
        "aid": False,
        "duration": "1 day per round",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "May–June",
        "eligibility": "US chemistry students",
        "website": "https://www.acs.org",
        "why_matters": "Chemistry specialty recognition, national competition experience."
    },
    {
        "id": 32,
        "name": "VEX Robotics Competition",
        "organization": "VEX Robotics",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Middle and high school robotics competition.",
        "full_description": "Team-based robotics with annual game challenges.",
        "cost": "Paid",
        "aid": True,
        "duration": "8 weeks (season)",
        "location": "On-campus",
        "country": "Global",
        "grades": ["6", "7", "8", "9", "10", "11", "12"],
        "application_window": "Ongoing",
        "eligibility": "School team",
        "website": "https://www.vexrobotics.com",
        "why_matters": "Accessible robotics, scalable complexity, global competition."
    },
    {
        "id": 33,
        "name": "Global Math Challenge",
        "organization": "MATHCOUNTS / American Mathematics Competitions",
        "level": "Accessible",
        "type": "Competition",
        "description": "Mathematics competition from middle school to high school levels.",
        "full_description": "AMC 8, AMC 10, AMC 12, and AIME for different skill levels.",
        "cost": "Free",
        "aid": False,
        "duration": "1.5 hours (test)",
        "location": "On-campus",
        "country": "USA",
        "grades": ["7", "8", "9", "10", "11", "12"],
        "application_window": "January–February",
        "eligibility": "Any student",
        "website": "https://www.maa.org/math-competitions",
        "why_matters": "Mathematical excellence recognition, gateway to math olympiad."
    },
    {
        "id": 34,
        "name": "High School Environmental STEM Project",
        "organization": "EPA / Local Environmental NGOs",
        "level": "Accessible",
        "type": "Research",
        "description": "Student-led environmental research and sustainability projects.",
        "full_description": "Design and execute environmental monitoring, conservation, or renewable energy projects.",
        "cost": "Free",
        "aid": False,
        "duration": "Semester / Year-long",
        "location": "On-campus",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Anytime",
        "eligibility": "Any student",
        "website": "https://www.epa.gov/students",
        "why_matters": "Real-world STEM application, environmental impact, community engagement."
    },
    {
        "id": 35,
        "name": "Udacity Nanodegree (High School Track)",
        "organization": "Udacity",
        "level": "Accessible",
        "type": "Online / Hybrid",
        "description": "Professional-grade online courses in tech and STEM fields.",
        "full_description": "Computer science, AI, cybersecurity, autonomous vehicles with project-based learning.",
        "cost": "Paid",
        "aid": False,
        "duration": "3–6 months",
        "location": "Online",
        "country": "Global",
        "grades": ["10", "11", "12"],
        "application_window": "Ongoing",
        "eligibility": "Any student",
        "website": "https://www.udacity.com",
        "why_matters": "Industry-recognized credentials, portfolio building, job readiness."
    },
    {
        "id": 36,
        "name": "Youth Mental Health Hackathon",
        "organization": "Mental Health Tech Org",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Hackathon focused on building tech solutions for mental health.",
        "full_description": "24–48 hour hackathon to code, design, or prototype mental health apps.",
        "cost": "Free",
        "aid": False,
        "duration": "24–48 hours",
        "location": "On-campus / Online",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "September–October",
        "eligibility": "Any student, team optional",
        "website": "https://mlh.io",
        "why_matters": "Real-world problem solving, portfolio project, social impact."
    },
    {
        "id": 37,
        "name": "Cornell Lab of Ornithology (Young Birder Program)",
        "organization": "Cornell Lab of Ornithology",
        "level": "Accessible",
        "type": "Research",
        "description": "Field biology and ornithology research for young scientists.",
        "full_description": "Learn bird identification, field research methods, and citizen science contributions.",
        "cost": "Free",
        "aid": False,
        "duration": "Self-paced / Field days",
        "location": "Online / On-field",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Anytime",
        "eligibility": "Any student",
        "website": "https://www.birds.cornell.edu",
        "why_matters": "Field biology skills, citizen science contribution, nature science bridge."
    },
    {
        "id": 38,
        "name": "International Junior Science Olympiad (IJSO)",
        "organization": "International Science Olympiad Organization",
        "level": "Accessible",
        "type": "Competition",
        "description": "International competition for younger/less advanced high school students.",
        "full_description": "Alternative to ISO with adjusted difficulty for grades 9–10.",
        "cost": "Free",
        "aid": False,
        "duration": "1 day (finals)",
        "location": "International",
        "country": "Global",
        "grades": ["9", "10"],
        "application_window": "September–October",
        "eligibility": "Grades 9–10",
        "website": "https://www.ijso.org",
        "why_matters": "Entry-level international competition, stepping stone to full ISO."
    },
    {
        "id": 39,
        "name": "CyberPatriot National Youth Cyber Defense Competition",
        "organization": "US Air Force Association",
        "level": "Accessible",
        "type": "Competition",
        "description": "High school cybersecurity competition and training.",
        "full_description": "Teams learn and practice cybersecurity defense of virtual computer networks.",
        "cost": "Free",
        "aid": False,
        "duration": "8 weeks (season)",
        "location": "Online",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "August–September",
        "eligibility": "School team",
        "website": "https://www.uscyberpatriot.org",
        "why_matters": "Cybersecurity career pathway, national recognition, skills-focused."
    },
    {
        "id": 40,
        "name": "Breakthrough Junior Challenge",
        "organization": "Breakthrough Prize Foundation",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "High school video competition explaining STEM concepts.",
        "full_description": "Create a short video explaining a big science or math idea; winning videos shown globally.",
        "cost": "Free",
        "aid": False,
        "duration": "2-month submission period",
        "location": "Online",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "July–September",
        "eligibility": "Any student",
        "website": "https://breakthroughjuniorchallenge.org",
        "why_matters": "Creative STEM expression, global platform, potential prize ($250K+)."
    },
    # ADDITIONAL TOP-TIER PROGRAMS
    {
        "id": 41,
        "name": "Oxford University Summer School",
        "organization": "University of Oxford",
        "level": "Top-Tier",
        "type": "Summer School",
        "description": "Intensive academic programs in sciences, mathematics, and engineering at Oxford.",
        "full_description": "Study with Oxford faculty and researchers in subjects like physics, chemistry, computer science, and more.",
        "cost": "Paid",
        "aid": True,
        "duration": "2-6 weeks",
        "location": "On-campus",
        "country": "UK",
        "grades": ["11", "12"],
        "application_window": "January–March",
        "eligibility": "Strong academics, international students welcome",
        "website": "https://www.ox.ac.uk/summer-schools",
        "why_matters": "World-class UK education, global network, college-level experience."
    },
    {
        "id": 42,
        "name": "Cambridge Science Festival Summer School",
        "organization": "University of Cambridge",
        "level": "Top-Tier",
        "type": "Summer School",
        "description": "STEM immersion program at Cambridge University.",
        "full_description": "Hands-on research, lab work, and seminars with Cambridge faculty.",
        "cost": "Paid",
        "aid": True,
        "duration": "2-4 weeks",
        "location": "On-campus",
        "country": "UK",
        "grades": ["11", "12"],
        "application_window": "February–April",
        "eligibility": "High academic achievement",
        "website": "https://www.cam.ac.uk/summer-schools",
        "why_matters": "Prestigious UK credential, research exposure, college preparation."
    },
    {
        "id": 43,
        "name": "Yale Young Global Scholars (YYGS)",
        "organization": "Yale University",
        "level": "Top-Tier",
        "type": "Summer School",
        "description": "Interdisciplinary program with STEM focus at Yale.",
        "full_description": "Explore STEM, policy, and innovation with students from 150+ countries.",
        "cost": "Paid",
        "aid": True,
        "duration": "2 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "November–February",
        "eligibility": "Strong academics, leadership experience",
        "website": "https://globalscholars.yale.edu",
        "why_matters": "Ivy League experience, global cohort, interdisciplinary learning."
    },
    {
        "id": 44,
        "name": "Research Science Institute (RSI)",
        "organization": "MIT & Center for Excellence in Education",
        "level": "Top-Tier",
        "type": "Research",
        "description": "The most prestigious free summer research program for high school students.",
        "full_description": "Six weeks of intensive research mentorship with world-class scientists at MIT.",
        "cost": "Free",
        "aid": False,
        "duration": "6 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "December–January",
        "eligibility": "Top 1% globally, exceptional STEM achievement",
        "website": "https://www.cee.org/rsi",
        "why_matters": "Most selective program globally, research publication potential, elite credential."
    },
    {
        "id": 45,
        "name": "International Mathematical Olympiad (IMO)",
        "organization": "International Mathematical Union",
        "level": "Top-Tier",
        "type": "Competition",
        "description": "The world championship mathematics competition for high school students.",
        "full_description": "Annual competition with 6 challenging math problems over 2 days.",
        "cost": "Free",
        "aid": False,
        "duration": "1 week",
        "location": "International",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "September–May (national rounds)",
        "eligibility": "Selected through national competitions",
        "website": "https://www.imo-official.org",
        "why_matters": "Most prestigious math competition globally, international recognition."
    },
    # ADDITIONAL ACHIEVABLE PROGRAMS
    {
        "id": 46,
        "name": "Columbia Science Honors Program",
        "organization": "Columbia University",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Saturday enrichment program in science and mathematics.",
        "full_description": "College-level courses in physics, chemistry, biology, computer science, and math.",
        "cost": "Free",
        "aid": False,
        "duration": "Academic year (Saturdays)",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "January–March",
        "eligibility": "NYC area students, competitive entrance exam",
        "website": "https://www.columbia.edu/shp",
        "why_matters": "Free Ivy League education, rigorous curriculum, weekend commitment."
    },
    {
        "id": 47,
        "name": "Duke TIP Summer Studies",
        "organization": "Duke University",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Intensive academic programs for gifted students.",
        "full_description": "Advanced STEM courses including engineering, biology, and computer science.",
        "cost": "Paid",
        "aid": True,
        "duration": "3 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "January–April",
        "eligibility": "Strong academics, talent search qualification",
        "website": "https://tip.duke.edu",
        "why_matters": "Gifted education, fast-paced learning, residential experience."
    },
    {
        "id": 48,
        "name": "Northwestern CTD Summer Programs",
        "organization": "Northwestern University",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Center for Talent Development STEM programs.",
        "full_description": "Advanced courses in science, engineering, and mathematics.",
        "cost": "Paid",
        "aid": True,
        "duration": "3 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "February–May",
        "eligibility": "Talent search qualification or strong academics",
        "website": "https://www.ctd.northwestern.edu",
        "why_matters": "Accelerated learning, university resources, college credit."
    },
    {
        "id": 49,
        "name": "Carnegie Mellon SAMS",
        "organization": "Carnegie Mellon University",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Summer Academy for Math and Science for underrepresented students.",
        "full_description": "Free program with advanced math, science, and college preparation.",
        "cost": "Free",
        "aid": False,
        "duration": "6 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "December–February",
        "eligibility": "Underrepresented minorities, strong academics",
        "website": "https://www.cmu.edu/sams",
        "why_matters": "Free top-tier education, diversity focus, college access."
    },
    {
        "id": 50,
        "name": "American Mathematics Competitions (AMC)",
        "organization": "Mathematical Association of America",
        "level": "Achievable",
        "type": "Competition",
        "description": "Series of math competitions leading to USAMO and IMO.",
        "full_description": "AMC 10/12 tests are the first step toward national and international math competitions.",
        "cost": "Free",
        "aid": False,
        "duration": "1 day",
        "location": "School-based",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "November–February",
        "eligibility": "Any student",
        "website": "https://maa.org/amc",
        "why_matters": "Pathway to elite math competitions, skill development."
    },
    # ADDITIONAL ACCESSIBLE PROGRAMS
    {
        "id": 51,
        "name": "edX High School Courses",
        "organization": "edX / MIT & Harvard",
        "level": "Accessible",
        "type": "Online / Hybrid",
        "description": "Free online courses from top universities.",
        "full_description": "Courses in computer science, engineering, biology, physics, and more.",
        "cost": "Free",
        "aid": False,
        "duration": "Self-paced",
        "location": "Online",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Anytime",
        "eligibility": "Any student",
        "website": "https://www.edx.org",
        "why_matters": "Free university-level learning, certificates available, flexible."
    },
    {
        "id": 52,
        "name": "Brilliant.org Interactive STEM",
        "organization": "Brilliant",
        "level": "Accessible",
        "type": "Online / Hybrid",
        "description": "Interactive problem-solving in math, science, and computer science.",
        "full_description": "Guided courses with hands-on problem solving in all STEM fields.",
        "cost": "Paid (Financial Aid Available)",
        "aid": True,
        "duration": "Self-paced",
        "location": "Online",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Anytime",
        "eligibility": "Any student",
        "website": "https://brilliant.org",
        "why_matters": "Interactive learning, problem-solving focus, strong pedagogy."
    },
    {
        "id": 53,
        "name": "Google Code-in (Archived) / Google Summer of Code",
        "organization": "Google",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Open source development for students.",
        "full_description": "Work on real open-source projects with mentors.",
        "cost": "Free",
        "aid": False,
        "duration": "3 months",
        "location": "Online",
        "country": "Global",
        "grades": ["10", "11", "12"],
        "application_window": "March–April",
        "eligibility": "Any student with coding experience",
        "website": "https://summerofcode.withgoogle.com",
        "why_matters": "Real-world coding, open source contribution, stipend."
    },
    {
        "id": 54,
        "name": "Microsoft Imagine Cup",
        "organization": "Microsoft",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Global technology competition for student innovators.",
        "full_description": "Build tech solutions for real-world problems with Azure cloud.",
        "cost": "Free",
        "aid": False,
        "duration": "6 months",
        "location": "Online",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "September–March",
        "eligibility": "Any student team",
        "website": "https://imaginecup.microsoft.com",
        "why_matters": "Industry recognition, mentorship, prizes up to $100K."
    },
    {
        "id": 55,
        "name": "Intel International Science and Engineering Fair (ISEF)",
        "organization": "Society for Science",
        "level": "Achievable",
        "type": "Competition",
        "description": "The world's largest pre-college STEM competition.",
        "full_description": "Present original research to judges and compete for millions in prizes.",
        "cost": "Free",
        "aid": False,
        "duration": "1 week",
        "location": "International",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "September–May (local/regional fairs)",
        "eligibility": "Qualify through affiliated fairs",
        "website": "https://www.societyforscience.org/isef",
        "why_matters": "Largest science fair globally, major scholarships, college admissions boost."
    },
    {
        "id": 56,
        "name": "Davidson Fellows Scholarship",
        "organization": "Davidson Institute",
        "level": "Achievable",
        "type": "Competition",
        "description": "Awards for extraordinary accomplishments by students 18 and under.",
        "full_description": "Submit significant work in STEM, literature, music, or other fields for up to $50K scholarship.",
        "cost": "Free",
        "aid": False,
        "duration": "Application process",
        "location": "Online",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "February",
        "eligibility": "Significant original work",
        "website": "https://www.davidsongifted.org/fellows",
        "why_matters": "Major scholarship, recognition of excellence, portfolio credential."
    },
    {
        "id": 57,
        "name": "USA Biology Olympiad (USABO)",
        "organization": "Center for Excellence in Education",
        "level": "Achievable",
        "type": "Competition",
        "description": "National biology competition leading to International Biology Olympiad.",
        "full_description": "Test biology knowledge and compete for national team selection.",
        "cost": "Free",
        "aid": False,
        "duration": "1 day",
        "location": "School-based",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "February–March",
        "eligibility": "Any US student",
        "website": "https://www.usabo-trc.org",
        "why_matters": "Biology excellence recognition, national team pathway."
    },
    {
        "id": 58,
        "name": "USA Computing Olympiad (USACO)",
        "organization": "USA Computing Olympiad",
        "level": "Achievable",
        "type": "Competition",
        "description": "Programming competition for high school students.",
        "full_description": "Four divisions (Bronze to Platinum) with algorithmic programming challenges.",
        "cost": "Free",
        "aid": False,
        "duration": "Year-round contests",
        "location": "Online",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Anytime",
        "eligibility": "Any US student",
        "website": "http://www.usaco.org",
        "why_matters": "Programming skill development, college admissions signal."
    },
    {
        "id": 59,
        "name": "USA Physics Olympiad (USAPhO)",
        "organization": "American Association of Physics Teachers",
        "level": "Achievable",
        "type": "Competition",
        "description": "National physics competition leading to International Physics Olympiad.",
        "full_description": "Challenging physics problems and experiments.",
        "cost": "Free",
        "aid": False,
        "duration": "1 day",
        "location": "School-based",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "January–March",
        "eligibility": "Any US student",
        "website": "https://aapt.org/physicsteam",
        "why_matters": "Physics mastery, national team pathway, college credential."
    },
    {
        "id": 60,
        "name": "USA Chemistry Olympiad (USNCO)",
        "organization": "American Chemical Society",
        "level": "Achievable",
        "type": "Competition",
        "description": "National chemistry competition leading to International Chemistry Olympiad.",
        "full_description": "Multi-tiered competition testing chemistry knowledge and laboratory skills.",
        "cost": "Free",
        "aid": False,
        "duration": "1 day",
        "location": "School-based",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "March–April",
        "eligibility": "Any US student",
        "website": "https://www.acs.org/olympiad",
        "why_matters": "Chemistry excellence, national team selection, college boost."
    },
    {
        "id": 61,
        "name": "Conrad Challenge",
        "organization": "Conrad Foundation",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Innovation competition for students to solve global problems.",
        "full_description": "Develop products or services addressing aerospace, energy, health, or other challenges.",
        "cost": "Free",
        "aid": False,
        "duration": "6 months",
        "location": "Online",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "September–April",
        "eligibility": "Any student team",
        "website": "https://www.conradchallenge.org",
        "why_matters": "Entrepreneurship experience, innovation skills, prizes."
    },
    {
        "id": 62,
        "name": "Diamond Challenge",
        "organization": "University of Delaware",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Entrepreneurship competition for high school students.",
        "full_description": "Pitch business ideas and compete for $100K+ in prizes.",
        "cost": "Free",
        "aid": False,
        "duration": "5 months",
        "location": "Online + Finals on-campus",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "November–March",
        "eligibility": "Any student team",
        "website": "https://diamondchallenge.org",
        "why_matters": "Business skills, pitch experience, major prizes."
    },
    {
        "id": 63,
        "name": "NSLC STEM Programs",
        "organization": "National Student Leadership Conference",
        "level": "Accessible",
        "type": "Summer School",
        "description": "Leadership and STEM programs at universities nationwide.",
        "full_description": "Hands-on programs in engineering, medicine, forensics, and technology.",
        "cost": "Paid",
        "aid": True,
        "duration": "1-2 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Rolling",
        "eligibility": "Any student",
        "website": "https://www.nslcleaders.org",
        "why_matters": "Career exploration, leadership development, residential experience."
    },
    {
        "id": 64,
        "name": "iD Tech Summer Camps",
        "organization": "iD Tech",
        "level": "Accessible",
        "type": "Summer School",
        "description": "Technology camps at top universities.",
        "full_description": "Coding, game design, robotics, and AI programs.",
        "cost": "Paid",
        "aid": True,
        "duration": "1-2 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Rolling",
        "eligibility": "Any student",
        "website": "https://www.idtech.com",
        "why_matters": "Tech skills, project-based learning, university setting."
    },
    {
        "id": 65,
        "name": "National Youth Science Camp (NYSCamp)",
        "organization": "National Youth Science Foundation",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Free prestigious science camp in West Virginia.",
        "full_description": "Two delegates from each state attend month-long STEM immersion program.",
        "cost": "Free",
        "aid": False,
        "duration": "1 month",
        "location": "On-campus",
        "country": "USA",
        "grades": ["12"],
        "application_window": "February–March",
        "eligibility": "Top 2 students per state",
        "website": "https://nysf.com",
        "why_matters": "Elite selection, free program, national network."
    },
    {
        "id": 66,
        "name": "Governor's School Programs",
        "organization": "Various State Governments",
        "level": "Achievable",
        "type": "Summer School",
        "description": "State-funded summer enrichment programs.",
        "full_description": "Intensive academic programs in STEM fields at state universities.",
        "cost": "Free",
        "aid": False,
        "duration": "4-6 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "January–March",
        "eligibility": "State residents, competitive selection",
        "website": "https://www.ncogs.org",
        "why_matters": "Free state program, competitive selection, academic rigor."
    },
    {
        "id": 67,
        "name": "PROMYS (Program in Mathematics for Young Scientists)",
        "organization": "Boston University",
        "level": "Top-Tier",
        "type": "Summer School",
        "description": "Intensive number theory program for mathematically talented students.",
        "full_description": "Six weeks of deep mathematical exploration and problem-solving.",
        "cost": "Paid",
        "aid": True,
        "duration": "6 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "January–March",
        "eligibility": "Strong mathematical ability",
        "website": "https://promys.org",
        "why_matters": "Elite math program, deep theoretical exploration, college preparation."
    },
    {
        "id": 68,
        "name": "MIT Beaver Works Summer Institute",
        "organization": "MIT",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Hands-on engineering and technology program.",
        "full_description": "Build autonomous drones, cyber-physical systems, and more.",
        "cost": "Free",
        "aid": False,
        "duration": "4 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "February–April",
        "eligibility": "Strong STEM background",
        "website": "https://beaverworks.ll.mit.edu/CMS/bw/bwsi",
        "why_matters": "Free MIT program, hands-on engineering, project-based."
    },
    {
        "id": 69,
        "name": "SSP (Summer Science Program)",
        "organization": "Summer Science Program",
        "level": "Top-Tier",
        "type": "Summer School",
        "description": "Astrophysics and biochemistry research program.",
        "full_description": "Team-based research projects in orbital mechanics or genomics.",
        "cost": "Paid",
        "aid": True,
        "duration": "6 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "December–February",
        "eligibility": "Strong STEM achievement",
        "website": "https://summerscience.org",
        "why_matters": "Elite selective program, original research, tight-knit community."
    },
    {
        "id": 70,
        "name": "Clark Scholars Program",
        "organization": "Texas Tech University",
        "level": "Achievable",
        "type": "Research",
        "description": "Intensive summer research program.",
        "full_description": "Seven weeks of mentored research in STEM fields.",
        "cost": "Free",
        "aid": False,
        "duration": "7 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "January–February",
        "eligibility": "Strong academics, research interest",
        "website": "https://www.depts.ttu.edu/honors/academicsandenrichment/affiliatedandhighschool/clarks",
        "why_matters": "Free research experience, publication potential, stipend."
    },
    {
        "id": 71,
        "name": "Boston Leadership Institute",
        "organization": "Boston Leadership Institute",
        "level": "Accessible",
        "type": "Summer School",
        "description": "STEM research and leadership programs.",
        "full_description": "Programs in medicine, engineering, business, and science.",
        "cost": "Paid",
        "aid": True,
        "duration": "3 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Rolling",
        "eligibility": "Any student",
        "website": "https://bostonleadershipinstitute.com",
        "why_matters": "Research experience, career exploration, certificate."
    },
    {
        "id": 72,
        "name": "Garcia Center STARS",
        "organization": "Stony Brook University",
        "level": "Achievable",
        "type": "Research",
        "description": "Summer research program for talented students.",
        "full_description": "Seven weeks of hands-on research in biochemistry, molecular biology, or chemistry.",
        "cost": "Free",
        "aid": False,
        "duration": "7 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "January–March",
        "eligibility": "Strong science background",
        "website": "https://garcia.sunysb.edu",
        "why_matters": "Free research program, publication potential, college preparation."
    },
    {
        "id": 73,
        "name": "NIH Summer Internship Program",
        "organization": "National Institutes of Health",
        "level": "Achievable",
        "type": "Research",
        "description": "Biomedical research internships at NIH.",
        "full_description": "Work alongside NIH scientists in labs across the country.",
        "cost": "Free",
        "aid": False,
        "duration": "8-10 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "December–March",
        "eligibility": "Strong biology/chemistry background",
        "website": "https://www.training.nih.gov/programs/sip",
        "why_matters": "Government research experience, stipend, publication potential."
    },
    {
        "id": 74,
        "name": "NASA SEES Intern Program",
        "organization": "NASA",
        "level": "Accessible",
        "type": "Online / Hybrid",
        "description": "Virtual Earth and space science internship.",
        "full_description": "Online program studying climate change and Earth systems using NASA data.",
        "cost": "Free",
        "aid": False,
        "duration": "8 weeks",
        "location": "Online",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "February–March",
        "eligibility": "Any US student",
        "website": "https://www.nasa.gov/stem/murep/projects/sees.html",
        "why_matters": "NASA credential, climate science, virtual flexibility."
    },
    {
        "id": 75,
        "name": "TASP / TASS (Telluride Association)",
        "organization": "Telluride Association",
        "level": "Top-Tier",
        "type": "Summer School",
        "description": "Free humanities and STEM seminar programs.",
        "full_description": "Six-week intensive seminars on advanced topics with no cost.",
        "cost": "Free",
        "aid": False,
        "duration": "6 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "January–February",
        "eligibility": "Highly selective, essay-based application",
        "website": "https://www.tellurideassociation.org",
        "why_matters": "Completely free, highly selective, intellectual community."
    },
    {
        "id": 76,
        "name": "MathILy & MathILy-Er",
        "organization": "MathILy",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Intensive mathematics summer program.",
        "full_description": "Five weeks of advanced mathematics exploration and discovery.",
        "cost": "Paid",
        "aid": True,
        "duration": "5 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "December–April",
        "eligibility": "Strong mathematical interest",
        "website": "https://mathily.org",
        "why_matters": "Deep mathematical exploration, community of math enthusiasts."
    },
    {
        "id": 77,
        "name": "Wolfram Summer School",
        "organization": "Wolfram Research",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Computational science and technology program.",
        "full_description": "Learn Wolfram Language and work on computational projects.",
        "cost": "Free",
        "aid": False,
        "duration": "3 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "March–May",
        "eligibility": "Project-based application",
        "website": "https://www.wolframphysics.org/summer-school",
        "why_matters": "Computational skills, industry connection, project completion."
    },
    {
        "id": 78,
        "name": "App Inventor Summer Program",
        "organization": "MIT Media Lab",
        "level": "Accessible",
        "type": "Online / Hybrid",
        "description": "Learn mobile app development with MIT App Inventor.",
        "full_description": "Build Android apps with visual programming tools.",
        "cost": "Free",
        "aid": False,
        "duration": "Self-paced",
        "location": "Online",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Anytime",
        "eligibility": "Any student",
        "website": "http://appinventor.mit.edu",
        "why_matters": "Mobile development skills, MIT resource, beginner-friendly."
    },
    {
        "id": 79,
        "name": "HCSSiM (Hampshire College Summer Studies in Mathematics)",
        "organization": "Hampshire College",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Immersive mathematics program for curious students.",
        "full_description": "Six weeks of advanced mathematical exploration and problem-solving.",
        "cost": "Paid",
        "aid": True,
        "duration": "6 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "January–April",
        "eligibility": "Mathematical curiosity and interest",
        "website": "https://hcssim.org",
        "why_matters": "Deep math immersion, supportive community, exploration-focused."
    },
    {
        "id": 80,
        "name": "AwesomeMath Summer Program",
        "organization": "AwesomeMath",
        "level": "Achievable",
        "type": "Summer School",
        "description": "Problem-solving focused math camp.",
        "full_description": "Three-week intensive preparation for math competitions and olympiads.",
        "cost": "Paid",
        "aid": True,
        "duration": "3 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "December–June",
        "eligibility": "Interest in competitive mathematics",
        "website": "https://www.awesomemath.org",
        "why_matters": "Competition preparation, problem-solving skills, math community."
    },
    {
        "id": 81,
        "name": "Project Lead The Way (PLTW)",
        "organization": "PLTW",
        "level": "Accessible",
        "type": "Summer School",
        "description": "Engineering and biomedical science programs nationwide.",
        "full_description": "Hands-on project-based STEM curriculum taught at schools nationwide.",
        "cost": "Free",
        "aid": False,
        "duration": "Academic year",
        "location": "School-based",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Varies by school",
        "eligibility": "Schools must offer PLTW",
        "website": "https://www.pltw.org",
        "why_matters": "Engineering pathway, hands-on learning, college credit potential."
    },
    {
        "id": 82,
        "name": "Girls Who Code Summer Immersion Program",
        "organization": "Girls Who Code",
        "level": "Accessible",
        "type": "Summer School",
        "description": "Free coding program for high school girls.",
        "full_description": "Two-week intensive computer science program with industry mentorship.",
        "cost": "Free",
        "aid": False,
        "duration": "2 weeks",
        "location": "On-campus / Online",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "December–March",
        "eligibility": "Female or non-binary students",
        "website": "https://girlswhocode.com",
        "why_matters": "Diversity in tech, free program, industry connections."
    },
    {
        "id": 83,
        "name": "Kode With Klossy",
        "organization": "Karlie Kloss Foundation",
        "level": "Accessible",
        "type": "Summer School",
        "description": "Free coding camps for young women.",
        "full_description": "Two-week camps teaching web development and mobile app development.",
        "cost": "Free",
        "aid": False,
        "duration": "2 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "February–April",
        "eligibility": "Female or non-binary students",
        "website": "https://www.kodewithklossy.com",
        "why_matters": "Free coding education, diversity focus, beginner-friendly."
    },
    {
        "id": 84,
        "name": "AI4ALL Summer Programs",
        "organization": "AI4ALL",
        "level": "Achievable",
        "type": "Summer School",
        "description": "AI and machine learning programs for underrepresented students.",
        "full_description": "Learn AI fundamentals at top universities like Stanford, Princeton, and Berkeley.",
        "cost": "Free",
        "aid": False,
        "duration": "2-3 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["10", "11", "12"],
        "application_window": "January–April",
        "eligibility": "Underrepresented in AI, competitive selection",
        "website": "https://ai-4-all.org",
        "why_matters": "AI education, diversity initiative, university partnerships."
    },
    {
        "id": 85,
        "name": "THINK Scholars Program",
        "organization": "MIT",
        "level": "Top-Tier",
        "type": "Research",
        "description": "Science and engineering research program at MIT.",
        "full_description": "Six-week intensive research mentorship with MIT faculty and labs.",
        "cost": "Free",
        "aid": False,
        "duration": "6 weeks",
        "location": "On-campus",
        "country": "USA",
        "grades": ["11", "12"],
        "application_window": "November–January",
        "eligibility": "Top students globally, project proposal required",
        "website": "https://think.mit.edu",
        "why_matters": "Elite MIT program, original research, publication potential."
    },
    {
        "id": 86,
        "name": "Space Camp (US Space & Rocket Center)",
        "organization": "US Space & Rocket Center",
        "level": "Accessible",
        "type": "Summer School",
        "description": "Hands-on space and aviation training.",
        "full_description": "Astronaut training simulators, rocket building, and mission simulations.",
        "cost": "Paid",
        "aid": True,
        "duration": "1 week",
        "location": "On-campus",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Rolling",
        "eligibility": "Any student",
        "website": "https://www.spacecamp.com",
        "why_matters": "Space exploration experience, hands-on engineering, fun learning."
    },
    {
        "id": 87,
        "name": "SeaPerch Underwater Robotics",
        "organization": "RoboNation",
        "level": "Accessible",
        "type": "Competition",
        "description": "Build and race underwater ROVs.",
        "full_description": "Design, build, and pilot remotely operated underwater vehicles.",
        "cost": "Free",
        "aid": False,
        "duration": "Academic year",
        "location": "School-based",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "September–May",
        "eligibility": "School team",
        "website": "https://seaperch.org",
        "why_matters": "Marine engineering, teamwork, hands-on robotics."
    },
    {
        "id": 88,
        "name": "VEX Robotics Competition",
        "organization": "REC Foundation",
        "level": "Accessible",
        "type": "Competition",
        "description": "Design and build robots for competitive challenges.",
        "full_description": "Year-round robotics competitions with new game challenges annually.",
        "cost": "Paid",
        "aid": False,
        "duration": "Academic year",
        "location": "School-based / Regional events",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "August–April",
        "eligibility": "School team",
        "website": "https://www.vexrobotics.com",
        "why_matters": "Engineering competition, teamwork, global reach."
    },
    {
        "id": 89,
        "name": "eCYBERMISSION",
        "organization": "US Army Educational Outreach Program",
        "level": "Accessible",
        "type": "Competition",
        "description": "STEM competition focused on community problems.",
        "full_description": "Teams propose solutions to local problems using STEM.",
        "cost": "Free",
        "aid": False,
        "duration": "Academic year",
        "location": "Online",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "October–February",
        "eligibility": "Any US student team",
        "website": "https://www.ecybermission.com",
        "why_matters": "Community focus, problem-solving, prizes up to $10K."
    },
    {
        "id": 90,
        "name": "NSHSS Foundation Scholarships",
        "organization": "National Society of High School Scholars",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Various scholarships for STEM students.",
        "full_description": "Multiple scholarship opportunities for academic achievement and community service.",
        "cost": "Free",
        "aid": False,
        "duration": "Application process",
        "location": "Online",
        "country": "USA",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Rolling",
        "eligibility": "NSHSS members or any student depending on scholarship",
        "website": "https://www.nshss.org/scholarships",
        "why_matters": "Financial aid, merit recognition, multiple opportunities."
    },
    {
        "id": 91,
        "name": "Siemens Competition (Now Regeneron STS)",
        "organization": "Regeneron & Society for Science",
        "level": "Top-Tier",
        "type": "Competition",
        "description": "The most prestigious science research competition for high school seniors.",
        "full_description": "Present original research for scholarships up to $250K.",
        "cost": "Free",
        "aid": False,
        "duration": "Application + Finals week",
        "location": "Online + Washington DC",
        "country": "USA",
        "grades": ["12"],
        "application_window": "August–November",
        "eligibility": "Original independent research",
        "website": "https://www.societyforscience.org/regeneron-sts",
        "why_matters": "Most prestigious US science competition, major scholarships, elite recognition."
    },
    {
        "id": 92,
        "name": "Questbridge National College Match",
        "organization": "Questbridge",
        "level": "Achievable",
        "type": "Innovation / Entrepreneurship",
        "description": "Full scholarship program for low-income high-achieving students.",
        "full_description": "Match with partner colleges for full four-year scholarships.",
        "cost": "Free",
        "aid": False,
        "duration": "Application process",
        "location": "Online",
        "country": "USA",
        "grades": ["12"],
        "application_window": "August–October",
        "eligibility": "High-achieving, low-income students",
        "website": "https://www.questbridge.org",
        "why_matters": "Full college scholarships, access to elite institutions, financial aid."
    },
    {
        "id": 93,
        "name": "Jack Kent Cooke Scholarship",
        "organization": "Jack Kent Cooke Foundation",
        "level": "Top-Tier",
        "type": "Innovation / Entrepreneurship",
        "description": "Major scholarship for high-achieving students with financial need.",
        "full_description": "Up to $40K per year for college plus mentorship and support.",
        "cost": "Free",
        "aid": False,
        "duration": "Application process",
        "location": "Online",
        "country": "USA",
        "grades": ["12"],
        "application_window": "September–November",
        "eligibility": "High achievement + financial need",
        "website": "https://www.jkcf.org",
        "why_matters": "Major scholarship, ongoing support, prestige."
    },
    {
        "id": 94,
        "name": "Coca-Cola Scholars Program",
        "organization": "Coca-Cola Scholars Foundation",
        "level": "Achievable",
        "type": "Innovation / Entrepreneurship",
        "description": "Merit-based scholarship for leadership and community service.",
        "full_description": "$20K scholarships for well-rounded students with strong academics and service.",
        "cost": "Free",
        "aid": False,
        "duration": "Application process",
        "location": "Online",
        "country": "USA",
        "grades": ["12"],
        "application_window": "August–October",
        "eligibility": "Academic achievement + leadership + service",
        "website": "https://www.coca-colascholarsfoundation.org",
        "why_matters": "Significant scholarship, national recognition, leadership focus."
    },
    {
        "id": 95,
        "name": "Ronald McDonald House Charities Scholarships",
        "organization": "RMHC",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Scholarships for students in various categories.",
        "full_description": "Multiple scholarship programs including STEM and community service focus.",
        "cost": "Free",
        "aid": False,
        "duration": "Application process",
        "location": "Online",
        "country": "USA",
        "grades": ["12"],
        "application_window": "October–January",
        "eligibility": "Varies by program",
        "website": "https://www.rmhc.org/scholarships",
        "why_matters": "Accessible scholarships, various categories, community focus."
    },
    {
        "id": 96,
        "name": "Gates Scholarship",
        "organization": "Bill & Melinda Gates Foundation",
        "level": "Top-Tier",
        "type": "Innovation / Entrepreneurship",
        "description": "Full scholarship for exceptional minority students.",
        "full_description": "Covers full cost of attendance for underrepresented minority students.",
        "cost": "Free",
        "aid": False,
        "duration": "Application process",
        "location": "Online",
        "country": "USA",
        "grades": ["12"],
        "application_window": "August–September",
        "eligibility": "Minority students, high achievement, financial need",
        "website": "https://www.thegatesscholarship.org",
        "why_matters": "Full-ride scholarship, prestigious, life-changing opportunity."
    },
    {
        "id": 97,
        "name": "Dell Scholars Program",
        "organization": "Michael & Susan Dell Foundation",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Scholarship for students overcoming adversity.",
        "full_description": "$20K scholarship plus laptop, textbook credits, and ongoing support.",
        "cost": "Free",
        "aid": False,
        "duration": "Application process",
        "location": "Online",
        "country": "USA",
        "grades": ["12"],
        "application_window": "October–December",
        "eligibility": "Overcome obstacles, financial need, college-ready",
        "website": "https://www.dellscholars.org",
        "why_matters": "Scholarship + support, focuses on resilience, ongoing mentorship."
    },
    {
        "id": 98,
        "name": "Elks National Foundation Scholarship",
        "organization": "Elks National Foundation",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Merit-based scholarships for leadership and community service.",
        "full_description": "Scholarships from $4K to $50K based on academics, leadership, and financial need.",
        "cost": "Free",
        "aid": False,
        "duration": "Application process",
        "location": "Online",
        "country": "USA",
        "grades": ["12"],
        "application_window": "August–November",
        "eligibility": "US citizens, leadership, community service",
        "website": "https://www.elks.org/scholars",
        "why_matters": "Accessible application, range of awards, service focus."
    },
    {
        "id": 99,
        "name": "Horatio Alger Scholarship",
        "organization": "Horatio Alger Association",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Scholarships for students overcoming adversity.",
        "full_description": "Multiple scholarship levels from state ($10K) to national ($25K).",
        "cost": "Free",
        "aid": False,
        "duration": "Application process",
        "location": "Online",
        "country": "USA",
        "grades": ["12"],
        "application_window": "August–October",
        "eligibility": "Overcome adversity, financial need, strong character",
        "website": "https://scholars.horatioalger.org",
        "why_matters": "Focuses on resilience, accessible, substantial awards."
    },
    {
        "id": 100,
        "name": "Future Engineers Space Tool Challenge",
        "organization": "NASA & Future Engineers",
        "level": "Accessible",
        "type": "Innovation / Entrepreneurship",
        "description": "Design tools for astronauts and space missions.",
        "full_description": "Submit 3D designs for tools that could be used in space; winners get 3D printed on ISS.",
        "cost": "Free",
        "aid": False,
        "duration": "2-3 months",
        "location": "Online",
        "country": "Global",
        "grades": ["9", "10", "11", "12"],
        "application_window": "Varies annually",
        "eligibility": "Any student",
        "website": "https://www.futureengineers.org",
        "why_matters": "NASA challenge, 3D design skills, ISS connection, real-world impact."
    },
]

HIGHLIGHTS: List[Dict[str, str]] = [
    {
        "title": "State Robotics Champions",
        "detail": "Team Pulse 1427 placed first at the regional robotics invitational.",
    },
    {
        "title": "NASA Student Challenge",
        "detail": "Seniors prototyped lunar habitat concepts and presented to NASA mentors.",
    },
    {
        "title": "Community STEM Day",
        "detail": "Middle-school outreach with 300+ visitors for coding and maker labs.",
    },
]

contact_messages: List[Dict[str, str]] = []


@app.context_processor
def inject_globals():
    return {
        "school_name": SCHOOL_NAME,
        "current_year": datetime.utcnow().year,
    }


@app.route("/")
def index():
    return render_template(
        "index.html",
        highlights=HIGHLIGHTS,
        school_name=SCHOOL_NAME
    )


@app.route("/programs")
def programs_hub():
    """Programs hub/navigation page"""
    return render_template("programs_hub.html", school_name=SCHOOL_NAME)


@app.route("/programs/top-tier")
def programs_top_tier():
    """Top-Tier programs page"""
    top_tier = [p for p in GLOBAL_PROGRAMS if p["level"] == "Top-Tier"]
    return render_template("programs_top_tier.html", programs=top_tier, school_name=SCHOOL_NAME)


@app.route("/programs/achievable")
def programs_achievable():
    """Achievable programs page"""
    achievable = [p for p in GLOBAL_PROGRAMS if p["level"] == "Achievable"]
    return render_template("programs_achievable.html", programs=achievable, school_name=SCHOOL_NAME)


@app.route("/programs/accessible")
def programs_accessible():
    """Accessible programs page"""
    accessible = [p for p in GLOBAL_PROGRAMS if p["level"] == "Accessible"]
    return render_template("programs_accessible.html", programs=accessible, school_name=SCHOOL_NAME)


@app.route("/programs/<int:program_id>")
def program_detail(program_id):
    """Individual program detail page"""
    program = next((p for p in GLOBAL_PROGRAMS if p["id"] == program_id), None)
    if not program:
        return "Program not found", 404
    
    # Determine the tier URL for back button
    tier_level = program.get("level", "Accessible").lower().replace(" ", "-")
    if tier_level == "top-tier":
        tier_url = "/programs/top-tier"
    elif tier_level == "achievable":
        tier_url = "/programs/achievable"
    else:
        tier_url = "/programs/accessible"
    
    return render_template("program_detail.html", program=program, school_name=SCHOOL_NAME, tier_url=tier_url)


@app.route("/api/programs/filter")
def filter_programs():
    """API endpoint for filtering programs (AJAX)"""
    filters = {
        "level": request.args.getlist("level"),
        "type": request.args.getlist("type"),
        "cost": request.args.getlist("cost"),
        "duration": request.args.getlist("duration"),
        "location": request.args.getlist("location"),
        "grades": request.args.getlist("grades"),
        "search": request.args.get("search", "").lower(),
    }
    
    filtered = GLOBAL_PROGRAMS.copy()
    
    # Apply filters
    if filters["level"]:
        filtered = [p for p in filtered if p["level"] in filters["level"]]
    if filters["type"]:
        filtered = [p for p in filtered if p["type"] in filters["type"]]
    if filters["cost"]:
        filtered = [p for p in filtered if p["cost"] in filters["cost"]]
    if filters["duration"]:
        filtered = [p for p in filtered if p["duration"] in filters["duration"]]
    if filters["location"]:
        filtered = [p for p in filtered if p["location"] in filters["location"]]
    if filters["grades"]:
        filtered = [p for p in filtered if any(g in p["grades"] for g in filters["grades"])]
    if filters["search"]:
        filtered = [p for p in filtered if 
                   filters["search"] in p["name"].lower() or
                   filters["search"] in p["description"].lower() or
                   filters["search"] in p["organization"].lower()]
    
    return jsonify([{
        "id": p["id"],
        "name": p["name"],
        "organization": p["organization"],
        "level": p["level"],
        "type": p["type"],
        "description": p["description"],
        "cost": p["cost"],
        "duration": p["duration"],
        "location": p["location"],
        "application_window": p["application_window"]
    } for p in filtered])


@app.route("/programs")
def programs():
    return render_template("programs_overview.html", programs=GLOBAL_PROGRAMS)


@app.route("/programs/listing")
def programs_listing():
    """All programs listing page with filters"""
    return render_template("programs_listing.html", programs=GLOBAL_PROGRAMS, school_name=SCHOOL_NAME)


@app.route("/highlights")
def highlights_page():
    return render_template("highlights.html", highlights=HIGHLIGHTS)


@app.route("/admissions")
def admissions():
    return render_template("admissions.html", current_year=datetime.utcnow().year)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill in all fields before submitting.", "error")
            return redirect(url_for("contact"))

        contact_messages.append(
            {
                "name": name,
                "email": email,
                "message": message,
                "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            }
        )
        flash("Thanks for reaching out! We'll respond soon.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html", messages=contact_messages)


# ============================================================================
# ADMIN ROUTES
# ============================================================================

def is_admin():
    """Check if current user is admin"""
    user = get_current_user()
    return user and user.get('role') == 'admin'


@app.route("/admin/panel")
def admin_panel():
    """Admin dashboard - messages and stats"""
    if not is_admin():
        flash("You don't have permission to access this page.", "error")
        return redirect(url_for("dashboard"))
    
    # Get stats
    total_messages = len(contact_messages)
    total_users = len(users_db)
    total_programs = len(GLOBAL_PROGRAMS)
    
    return render_template(
        "admin_panel.html",
        messages=contact_messages,
        total_messages=total_messages,
        total_users=total_users,
        total_programs=total_programs,
        SCHOOL_NAME=SCHOOL_NAME
    )


@app.route("/admin/message/<int:msg_index>/delete", methods=["POST"])
def delete_message(msg_index):
    """Delete a contact message"""
    if not is_admin():
        return jsonify({"error": "Unauthorized"}), 403
    
    if 0 <= msg_index < len(contact_messages):
        deleted = contact_messages.pop(msg_index)
        flash(f"Message from {deleted['name']} deleted.", "success")
    
    return redirect(url_for("admin_panel"))


@app.route("/admin/message/<int:msg_index>/reply", methods=["GET", "POST"])
def reply_to_message(msg_index):
    """View message details and compose reply"""
    if not is_admin():
        flash("You don't have permission to access this page.", "error")
        return redirect(url_for("dashboard"))
    
    if not (0 <= msg_index < len(contact_messages)):
        flash("Message not found.", "error")
        return redirect(url_for("admin_panel"))
    
    message = contact_messages[msg_index]
    
    if request.method == "POST":
        # In production, this would send an actual email
        reply_text = request.form.get("reply_text", "").strip()
        if reply_text:
            flash(f"Reply prepared for {message['name']} ({message['email']}). In production, this would send an email.", "success")
            return redirect(url_for("admin_panel"))
    
    return render_template(
        "admin_reply.html",
        message=message,
        msg_index=msg_index,
        SCHOOL_NAME=SCHOOL_NAME
    )


@app.route("/admin/users")
def admin_users():
    """View all users"""
    if not is_admin():
        flash("You don't have permission to access this page.", "error")
        return redirect(url_for("dashboard"))
    
    users_list = list(users_db.values())
    return render_template(
        "admin_users.html",
        users=users_list,
        SCHOOL_NAME=SCHOOL_NAME
    )


@app.route("/admin/program/add", methods=["GET", "POST"])
def admin_add_program():
    """Add a new program"""
    if not is_admin():
        flash("You don't have permission to access this page.", "error")
        return redirect(url_for("dashboard"))
    
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        org = request.form.get("organization", "").strip()
        level = request.form.get("level", "").strip()
        prog_type = request.form.get("type", "").strip()
        cost = request.form.get("cost", "").strip()
        country = request.form.get("country", "").strip()
        
        if not all([name, org, level, prog_type, cost, country]):
            flash("Please fill in all required fields.", "error")
        else:
            new_id = max([p['id'] for p in GLOBAL_PROGRAMS]) + 1 if GLOBAL_PROGRAMS else 1
            new_program = {
                "id": new_id,
                "name": name,
                "organization": org,
                "level": level,
                "type": prog_type,
                "description": request.form.get("description", ""),
                "cost": cost,
                "aid": request.form.get("aid") == "on",
                "duration": request.form.get("duration", ""),
                "location": request.form.get("location", ""),
                "country": country,
                "grades": request.form.getlist("grades"),
                "application_window": request.form.get("application_window", ""),
                "eligibility": request.form.get("eligibility", ""),
                "website": request.form.get("website", ""),
                "why_matters": request.form.get("why_matters", ""),
            }
            GLOBAL_PROGRAMS.append(new_program)
            flash(f"Program '{name}' added successfully!", "success")
            return redirect(url_for("admin_panel"))
    
    return render_template(
        "admin_add_program.html",
        SCHOOL_NAME=SCHOOL_NAME
    )


@app.route("/writing")
def writing():
    # Redirect to the new basics page so navigation stays in sync with split pages
    return redirect(url_for("writing_basics"))


@app.route("/writing/basics")
def writing_basics():
    return render_template("writing_basics.html", school_name=SCHOOL_NAME)


@app.route("/writing/examples")
def writing_examples():
    return render_template("writing_examples.html", school_name=SCHOOL_NAME)


@app.route("/writing/resources")
def writing_resources():
    return render_template("writing_resources.html", school_name=SCHOOL_NAME)


# ========================================
# USER AUTHENTICATION SYSTEM
# ========================================

# Simple in-memory user storage (for demonstration)
# In production, use a proper database
users_db = {}
user_sessions = {}


def hash_password(password: str) -> str:
    """Hash a password for secure storage"""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against a hash"""
    return hash_password(password) == hashed


def get_current_user():
    """Get the currently logged-in user from session"""
    user_id = session.get('user_id')
    if user_id and user_id in users_db:
        return users_db[user_id]
    return None


def login_required(f):
    """Decorator to require login for certain routes"""
    from functools import wraps
    
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Redirect if already logged in
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == "POST":
        fullname = request.form.get("fullname", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()
        confirm_password = request.form.get("confirm_password", "").strip()
        role = request.form.get("role", "").strip()

        # Validation
        if not fullname or len(fullname) < 3:
            flash("Full name must be at least 3 characters.", "error")
            return redirect(url_for("signup"))

        if not email or "@" not in email:
            flash("Please enter a valid email address.", "error")
            return redirect(url_for("signup"))

        if email in [user['email'] for user in users_db.values()]:
            flash("An account with this email already exists.", "error")
            return redirect(url_for("signup"))

        if not password or len(password) < 8:
            flash("Password must be at least 8 characters.", "error")
            return redirect(url_for("signup"))

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for("signup"))

        # Create user - First user is always admin
        user_id = secrets.token_urlsafe(16)
        is_first_user = len(users_db) == 0
        users_db[user_id] = {
            'id': user_id,
            'name': fullname,
            'email': email,
            'password': hash_password(password),
            'role': 'admin' if is_first_user else (role or 'visitor'),
            'created_at': datetime.utcnow().isoformat(),
            'saved_programs': [],
            'bookmarked_resources': [],
            'days_active': 1
        }

        # Log the user in
        session['user_id'] = user_id
        session.permanent = True

        flash(f"Welcome, {fullname}! Your account has been created.", "success")
        return redirect(url_for('dashboard'))

    return render_template("signup.html", SCHOOL_NAME=SCHOOL_NAME)


@app.route("/login", methods=["GET", "POST"])
def login():
    # Redirect if already logged in
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()
        remember = request.form.get("remember") == "true"

        # Find user
        user = None
        for uid, u in users_db.items():
            if u['email'] == email:
                user = u
                break

        if not user:
            flash("No account found with that email address.", "error")
            return redirect(url_for("login"))

        if not verify_password(password, user['password']):
            flash("Incorrect password. Please try again.", "error")
            return redirect(url_for("login"))

        # Log the user in
        session['user_id'] = user['id']
        session.permanent = remember

        # Redirect to next page if specified
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)

        flash(f"Welcome back, {user['name'].split()[0]}!", "success")
        return redirect(url_for('dashboard'))

    return render_template("login.html", SCHOOL_NAME=SCHOOL_NAME)


@app.route("/logout")
def logout():
    session.pop('user_id', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('index'))


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()

        # In a real application, you would:
        # 1. Check if email exists
        # 2. Generate a secure reset token
        # 3. Send email with reset link
        # 4. Store token with expiration

        # For demonstration:
        user_exists = any(u['email'] == email for u in users_db.values())
        
        if user_exists:
            flash("Password reset instructions have been sent to your email.", "success")
        else:
            # Don't reveal if email exists for security
            flash("If an account exists with that email, you will receive reset instructions.", "info")
        
        return redirect(url_for('login'))

    return render_template("forgot_password.html", SCHOOL_NAME=SCHOOL_NAME)


@app.route("/dashboard")
@login_required
def dashboard():
    user = get_current_user()
    
    if not user:
        return redirect(url_for('login'))

    # Get saved programs (filter from GLOBAL_PROGRAMS)
    saved_programs = [
        prog for prog in GLOBAL_PROGRAMS 
        if prog['id'] in user['saved_programs']
    ]

    # Prepare bookmarked resources
    bookmarked_resources = user.get('bookmarked_resources', [])
    days_active = user.get('days_active', 1)

    return render_template(
        "dashboard.html",
        SCHOOL_NAME=SCHOOL_NAME,
        user=user,
        saved_programs=saved_programs,
        bookmarked_resources=bookmarked_resources,
        days_active=days_active
    )


# API endpoint to save/unsave programs
@app.route("/api/save-program/<int:program_id>", methods=["POST"])
@login_required
def save_program(program_id):
    user = get_current_user()
    
    if not user:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401

    # Check if program exists
    program = next((p for p in GLOBAL_PROGRAMS if p['id'] == program_id), None)
    if not program:
        return jsonify({'success': False, 'error': 'Program not found'}), 404

    # Toggle save status
    if program_id in user['saved_programs']:
        user['saved_programs'].remove(program_id)
        action = 'unsaved'
    else:
        user['saved_programs'].append(program_id)
        action = 'saved'

    return jsonify({
        'success': True,
        'action': action,
        'program_id': program_id
    })


# API endpoint to bookmark resources
@app.route("/api/bookmark-resource", methods=["POST"])
@login_required
def bookmark_resource():
    user = get_current_user()
    
    if not user:
        return jsonify({'success': False, 'error': 'Not logged in'}), 401

    data = request.get_json()
    resource = {
        'title': data.get('title'),
        'type': data.get('type'),
        'url': data.get('url')
    }

    # Check if already bookmarked
    if resource in user['bookmarked_resources']:
        user['bookmarked_resources'].remove(resource)
        action = 'removed'
    else:
        user['bookmarked_resources'].append(resource)
        action = 'added'

    return jsonify({
        'success': True,
        'action': action
    })


# Test route to quickly save programs (for development/testing)
@app.route("/test-save")
@login_required
def test_save():
    return render_template("test_save.html", SCHOOL_NAME=SCHOOL_NAME, programs=GLOBAL_PROGRAMS)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

