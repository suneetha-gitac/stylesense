import streamlit as st
from groq import Groq

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CurricuForge AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* { font-family: 'Inter', sans-serif; }

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0d1117, #0a1929, #0d2137);
    min-height: 100vh;
}

[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.03);
    border-right: 1px solid rgba(255,255,255,0.07);
    backdrop-filter: blur(20px);
}

.curri-header {
    background: linear-gradient(135deg, rgba(16,185,129,0.18), rgba(6,182,212,0.18));
    border: 1px solid rgba(16,185,129,0.35);
    border-radius: 20px;
    padding: 2.5rem;
    text-align: center;
    margin-bottom: 2rem;
    backdrop-filter: blur(10px);
}

.curri-header h1 {
    background: linear-gradient(90deg, #34d399, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3rem;
    font-weight: 800;
    margin: 0;
    letter-spacing: -1px;
}

.curri-header p {
    color: rgba(255,255,255,0.6);
    font-size: 1.1rem;
    margin-top: 0.5rem;
}

.result-box {
    background: rgba(10,25,41,0.95);
    border: 1px solid rgba(52,211,153,0.22);
    border-radius: 16px;
    padding: 1.5rem;
    margin-top: 1rem;
    color: #e2e8f0;
    line-height: 1.85;
    white-space: pre-wrap;
    font-size: 0.94rem;
}

.section-title {
    color: #34d399;
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 1rem;
    border-left: 4px solid #34d399;
    padding-left: 0.75rem;
}

.stButton > button {
    background: linear-gradient(135deg, #059669, #0891b2) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.6rem 2rem !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    transition: all 0.3s ease !important;
    width: 100%;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #047857, #0e7490) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 25px rgba(5,150,105,0.4) !important;
}

[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stSelectbox"] > div,
[data-testid="stNumberInput"] input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.13) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
}

label, .stMarkdown p { color: rgba(255,255,255,0.82) !important; }

.metric-badge {
    display: inline-block;
    background: rgba(52,211,153,0.12);
    border: 1px solid rgba(52,211,153,0.3);
    border-radius: 20px;
    padding: 0.25rem 0.75rem;
    font-size: 0.8rem;
    color: #34d399;
    font-weight: 600;
    margin: 0.2rem;
}

div[data-testid="stTabs"] button {
    color: rgba(255,255,255,0.55) !important;
    font-weight: 600 !important;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #34d399 !important;
    border-bottom-color: #34d399 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Model & Client ────────────────────────────────────────────────────────────
MODEL = "llama-3.3-70b-versatile"

def call_ai(prompt: str, system: str = "You are CurricuForge, an expert AI curriculum designer and instructional design specialist.") -> str:
    api_key = st.session_state.get("groq_api_key", "")
    if not api_key:
        return "⚠️ Please enter your Groq API key in the sidebar."
    try:
        client = Groq(api_key=api_key)
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            max_tokens=2000,
            temperature=0.5,
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div style="color:#34d399;font-size:1.1rem;font-weight:700;margin-bottom:1rem;">⚙️ Configuration</div>', unsafe_allow_html=True)
    groq_key = st.text_input("Groq API Key", type="password", placeholder="gsk_...")
    if groq_key:
        st.session_state["groq_api_key"] = groq_key

    st.markdown("---")
    st.markdown("""
    <div style='color:rgba(255,255,255,0.5); font-size:0.8rem;'>
    <b style='color:#34d399'>Model:</b> llama-3.3-70b-versatile<br><br>
    <b style='color:#34d399'>Features:</b><br>
    📚 Course Structure Generation<br>
    📋 Topic Recommendations<br>
    🗓️ Curriculum Planning<br>
    🎯 Learning Outcome Mapping<br>
    🏆 Academic Optimization<br>
    💬 Curriculum Assistant
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<span class="metric-badge">Llama 3.3-70B</span><span class="metric-badge">Groq</span>', unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="curri-header">
    <h1>🎓 CurricuForge AI</h1>
    <p>Generative AI–Powered Curriculum Design System</p>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tabs = st.tabs(["📚 Course Structure", "📋 Topic Recommendations", "🗓️ Curriculum Planning", "🎯 Learning Outcomes", "🏆 Academic Optimization", "💬 Curriculum Assistant"])

# ── Tab 1: Course Structure Generation ───────────────────────────────────────
with tabs[0]:
    st.markdown('<div class="section-title">📚 Course Structure Generator</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        course_name = st.text_input("Course Title", placeholder="e.g. Introduction to Machine Learning")
        subject_area = st.text_input("Subject / Domain", placeholder="e.g. Computer Science, Business, Healthcare")
        level = st.selectbox("Academic Level", ["School (K-12)", "Undergraduate", "Postgraduate", "Doctoral", "Professional Certification", "Online / MOOC"])
    with col2:
        duration = st.selectbox("Course Duration", ["1 Week Bootcamp", "4 Weeks", "8 Weeks", "1 Semester (16 Weeks)", "1 Year", "2 Years"])
        credits = st.number_input("Credit Hours (if applicable)", min_value=0, max_value=30, value=3)
        delivery = st.selectbox("Delivery Mode", ["In-Person", "Online (Async)", "Online (Sync)", "Hybrid", "Self-Paced"])

    prerequisites = st.text_input("Prerequisites", placeholder="e.g. Basic Python, Linear Algebra, Statistics 101")
    target_learners = st.text_area("Target Learner Profile", placeholder="Describe your ideal student...", height=70)

    if st.button("📚 Generate Course Structure", key="course_struct"):
        with st.spinner("Designing your course structure..."):
            prompt = f"""Design a comprehensive course structure for:

Course Title: {course_name}
Subject / Domain: {subject_area}
Academic Level: {level}
Duration: {duration}
Credit Hours: {credits}
Delivery Mode: {delivery}
Prerequisites: {prerequisites if prerequisites else 'None'}
Target Learner: {target_learners if target_learners else 'General learners'}

Provide:
1. Course Overview & Rationale
2. Course Objectives (5-7 SMART objectives)
3. Module-by-Module Breakdown:
   - Module name & description
   - Key topics per module
   - Activities / Assignments
   - Duration / Weeks
4. Instructional Methods & Resources
5. Assessment Strategy
   - Formative assessments
   - Summative assessments (with weightage %)
6. Required & Recommended Textbooks/Resources
7. Grading Policy
8. Industry Alignment & Relevance

Format it like a professional course syllabus."""
            result = call_ai(prompt)
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

# ── Tab 2: Topic Recommendations ─────────────────────────────────────────────
with tabs[1]:
    st.markdown('<div class="section-title">📋 AI Topic Recommendation Engine</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        tr_subject = st.text_input("Subject / Discipline", placeholder="e.g. Data Science, Civil Engineering, Marketing")
        tr_level = st.selectbox("Course Level", ["Beginner", "Intermediate", "Advanced", "Expert"])
        tr_industry = st.text_input("Target Industry", placeholder="e.g. FinTech, Healthcare, EdTech, Manufacturing")
    with col2:
        tr_year = st.selectbox("Academic Year", ["2024-25", "2025-26", "2026-27"])
        tr_duration = st.number_input("Number of Topics Needed", min_value=5, max_value=60, value=20)
        tr_trends = st.checkbox("Include Latest Industry Trends", value=True)

    tr_existing = st.text_area("Existing Topics (to avoid duplication)", placeholder="List topics already covered in prerequisite courses...", height=80)

    if st.button("📋 Generate Topic Recommendations", key="topics"):
        with st.spinner("Curating AI-powered topic recommendations..."):
            prompt = f"""Generate comprehensive topic recommendations for a {tr_level}-level course in {tr_subject} targeting the {tr_industry} industry.

Academic Year: {tr_year}
Number of Topics: {tr_duration}
Include Industry Trends: {tr_trends}
Existing Topics to Avoid: {tr_existing if tr_existing else 'None'}

Provide:
1. Core Essential Topics (must-have foundational topics)
2. Advanced Elective Topics (depth topics for deeper specialization)
3. Emerging & Trending Topics (cutting-edge, industry-relevant, 2024-25 onwards)
4. Practical / Lab / Project Topics
5. Soft Skills & Professional Development Topics
6. Cross-Disciplinary Integration Topics

For each topic include:
- Topic Name
- Brief Description (2 lines)
- Why it's relevant for {tr_industry}
- Recommended resources (1 book, 1 online resource)
- Estimated teaching hours
- Skill level tag

Sort by recommended teaching sequence."""
            result = call_ai(prompt, system="You are an expert curriculum designer and academic advisor with deep knowledge of industry trends and educational best practices.")
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

# ── Tab 3: Curriculum Planning ────────────────────────────────────────────────
with tabs[2]:
    st.markdown('<div class="section-title">🗓️ Full Curriculum Planner</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        cp_program = st.text_input("Program Name", placeholder="e.g. B.Tech Computer Science & Engineering")
        cp_duration = st.selectbox("Program Duration", ["6 Months", "1 Year", "2 Years", "3 Years", "4 Years"])
        cp_type = st.selectbox("Program Type", ["Full-Time", "Part-Time", "Online", "Executive", "Vocational"])
    with col2:
        cp_affiliation = st.text_input("University / Institution Type", placeholder="e.g. AICTE-affiliated, UGC, Autonomous, International")
        cp_specialization = st.text_input("Specialization / Concentration", placeholder="e.g. AI & Data Science, Finance, Clinical Research")
        cp_accreditation = st.selectbox("Accreditation Framework", ["NBA (India)", "NAAC (India)", "ABET (USA)", "EQUIS (Europe)", "QAA (UK)", "None"])

    cp_goals = st.text_area("Program Educational Objectives", placeholder="What should graduates be able to do?", height=80)

    if st.button("🗓️ Generate Curriculum Plan", key="curriculum"):
        with st.spinner("Building your full curriculum plan..."):
            prompt = f"""Design a complete curriculum plan for:

Program: {cp_program}
Duration: {cp_duration}
Type: {cp_type}
Institution: {cp_affiliation}
Specialization: {cp_specialization}
Accreditation: {cp_accreditation}
Program Goals: {cp_goals if cp_goals else 'Standard academic goals'}

Create a detailed curriculum including:
1. Program Overview & Vision
2. Program Educational Objectives (PEOs) — Bloom's Taxonomy aligned
3. Graduate Attributes
4. Semester-wise / Year-wise Course Layout:
   - Core courses with credit hours
   - Elective courses / tracks
   - Lab & practical components
   - Project-based learning components
   - Internship / Industry attachment
   - Capstone project
5. Curriculum Map (Course vs Outcome matrix)
6. Industry Integration Points
7. Assessment Framework aligned to {cp_accreditation}
8. Co-curricular & Extra-curricular inclusions
9. Total Credit Hours Summary
10. Comparison with global best practices

Format as a comprehensive academic document."""
            result = call_ai(prompt)
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

# ── Tab 4: Learning Outcome Mapping ──────────────────────────────────────────
with tabs[3]:
    st.markdown('<div class="section-title">🎯 Learning Outcome Mapper</div>', unsafe_allow_html=True)
    st.info("Map your course content to learning outcomes using Bloom's Taxonomy and industry competency frameworks.", icon="🎯")
    col1, col2 = st.columns(2)
    with col1:
        lo_course = st.text_input("Course / Module Name", placeholder="e.g. Advanced Database Systems")
        lo_bloom = st.multiselect("Bloom's Taxonomy Levels to Target", ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"], default=["Understand", "Apply", "Analyze"])
    with col2:
        lo_framework = st.selectbox("Competency Framework", ["Bloom's Taxonomy", "OBE (Outcome-Based Education)", "ABET Student Outcomes", "Dublin Descriptors", "NZQF", "Custom"])
        lo_industry = st.text_input("Industry Skill Framework (optional)", placeholder="e.g. NASSCOM, IEEE, PMI, SHRM")

    lo_topics = st.text_area("Course Topics / Content", placeholder="List the topics, chapters, or content covered in this course...", height=120)

    if st.button("🎯 Map Learning Outcomes", key="outcomes"):
        with st.spinner("Mapping learning outcomes..."):
            prompt = f"""Create a comprehensive Learning Outcome mapping for:

Course: {lo_course}
Bloom's Levels: {', '.join(lo_bloom)}
Framework: {lo_framework}
Industry Framework: {lo_industry if lo_industry else 'None'}
Course Topics:
{lo_topics}

Generate:
1. Course Learning Outcomes (CLOs) — 6-8 measurable outcomes
   - Each aligned to specific Bloom's taxonomy level
   - Written with action verbs (Know/Understand/Apply/Analyze/Evaluate/Create)
2. Topic-to-CLO Mapping Table
3. CLO-to-PO (Program Outcome) Mapping Matrix
4. Assessment Mapping (which CLO is assessed by which instrument)
5. Attainment Measurement Strategy
   - Direct assessment methods
   - Indirect assessment methods
   - Target attainment levels (%)
6. Industry Competency Alignment (if framework specified)
7. Gap Analysis & Recommendations

Format as a structured OBE document with tables."""
            result = call_ai(prompt, system="You are an expert in Outcome-Based Education (OBE), instructional design, and academic quality assurance. Create precise, measurable, and industry-aligned learning outcomes.")
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

# ── Tab 5: Academic Optimization ─────────────────────────────────────────────
with tabs[4]:
    st.markdown('<div class="section-title">🏆 Academic Program Optimizer</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        ao_program = st.text_area("Current Program Description", placeholder="Describe your existing program, courses, or curriculum...", height=120)
        ao_issue = st.multiselect("Key Challenges to Address", [
            "Low student engagement",
            "Poor industry alignment",
            "High dropout/failure rates",
            "Outdated content",
            "Weak practical component",
            "Assessment gaps",
            "Accreditation gaps",
        ])
    with col2:
        ao_benchmark = st.text_input("Benchmark Institution / Program", placeholder="e.g. MIT EECS, IIT Bombay CSE, Stanford MBA")
        ao_goal = st.text_area("Optimization Goals", placeholder="What outcomes do you want to improve?", height=120)

    if st.button("🏆 Optimize Academic Program", key="optimize"):
        with st.spinner("Generating optimization recommendations..."):
            prompt = f"""Perform a comprehensive academic program optimization analysis:

Current Program:
{ao_program}

Key Challenges: {', '.join(ao_issue) if ao_issue else 'General quality improvement'}
Benchmark Against: {ao_benchmark if ao_benchmark else 'Global best practices'}
Optimization Goals: {ao_goal if ao_goal else 'Overall program quality'}

Provide:
1. Program Health Assessment (Score out of 100)
   - Content Relevance
   - Industry Alignment
   - Assessment Quality
   - Learner Experience
   - Graduate Outcomes
2. Benchmarking Analysis (vs {ao_benchmark if ao_benchmark else 'global leaders'})
3. Gap Analysis — Top 10 gaps identified
4. Quick Wins (improvements achievable within 1 semester)
5. Strategic Recommendations (1-2 year roadmap)
6. Curriculum Redesign Suggestions
7. Industry Partnership Recommendations
8. Technology Integration Plan (EdTech tools, LMS, simulations)
9. Faculty Development Needs
10. Student Support Enhancements
11. Expected Impact Metrics after optimization

Be specific, data-driven, and actionable."""
            result = call_ai(prompt, system="You are an academic quality assurance expert, accreditation consultant, and curriculum innovation specialist.")
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

# ── Tab 6: Curriculum Assistant ───────────────────────────────────────────────
with tabs[5]:
    st.markdown('<div class="section-title">💬 AI Curriculum Assistant</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:rgba(255,255,255,0.5);font-size:0.9rem;">Ask anything about curriculum design, accreditation, OBE, pedagogy, or academic planning.</p>', unsafe_allow_html=True)

    if "curri_chat" not in st.session_state:
        st.session_state.curri_chat = []

    for msg in st.session_state.curri_chat:
        if msg["role"] == "user":
            st.markdown(f"""<div style="background:rgba(5,150,105,0.18);border:1px solid rgba(5,150,105,0.3);border-radius:12px;padding:0.75rem 1rem;margin:0.5rem 0;color:#e2e8f0;">
            <b style="color:#34d399">You:</b> {msg['content']}</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:12px;padding:0.75rem 1rem;margin:0.5rem 0;color:#e2e8f0;">
            <b style="color:#38bdf8">CurricuForge AI:</b> {msg['content']}</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input("Ask your curriculum question...", placeholder="e.g. How do I align my course to OBE standards?", key="curri_input", label_visibility="collapsed")
    with col2:
        send = st.button("Send →", key="curri_send")

    if send and user_input:
        st.session_state.curri_chat.append({"role": "user", "content": user_input})
        history_prompt = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.curri_chat[-6:]])
        with st.spinner("Thinking..."):
            response = call_ai(history_prompt, system="You are CurricuForge, an expert AI curriculum designer with deep expertise in OBE, Bloom's Taxonomy, accreditation frameworks (NBA, NAAC, ABET), instructional design, and academic best practices. Provide clear, structured, and actionable guidance.")
        st.session_state.curri_chat.append({"role": "assistant", "content": response})
        st.rerun()

    if st.button("🗑️ Clear Chat", key="curri_clear"):
        st.session_state.curri_chat = []
        st.rerun()

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:rgba(255,255,255,0.3); font-size:0.8rem; padding:1rem 0;">
    🎓 CurricuForge AI — Powered by <b style="color:#34d399">llama-3.3-70b-versatile</b> via Groq &nbsp;|&nbsp; Built with Streamlit
</div>
""", unsafe_allow_html=True)
