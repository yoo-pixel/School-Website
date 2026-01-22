// ========================================
// HEADER SCROLL EFFECTS & NAVIGATION
// ========================================

const header = document.getElementById('mainHeader');
const navToggle = document.getElementById('navToggle');
const nav = document.getElementById('nav');

// Header scroll effect
let lastScroll = 0;
window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }

    lastScroll = currentScroll;
});

// Mobile navigation toggle
if (navToggle && nav) {
    navToggle.addEventListener('click', () => {
        nav.classList.toggle('nav--open');
        navToggle.classList.toggle('active');
    });
}

// ========================================
// THEME TOGGLE (DARK/LIGHT MODE)
// ========================================

const themeToggle = document.getElementById('themeToggle');
const body = document.body;

// Load saved theme or default to dark
const savedTheme = localStorage.getItem('theme') || 'dark-mode';
body.classList.add(savedTheme);

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        if (body.classList.contains('dark-mode')) {
            body.classList.remove('dark-mode');
            body.classList.add('light-mode');
            localStorage.setItem('theme', 'light-mode');
        } else {
            body.classList.remove('light-mode');
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark-mode');
        }
    });
}

// ========================================
// LANGUAGE TOGGLE (ENGLISH/ARABIC)
// ========================================

const langToggle = document.getElementById('langToggle');
const savedLang = localStorage.getItem('language') || 'en';
document.documentElement.setAttribute('lang', savedLang);
document.documentElement.setAttribute('dir', savedLang === 'ar' ? 'rtl' : 'ltr');

// Language translations
const translations = {
    en: {
        home: 'Home',
        programs: 'Programs',
        highlights: 'Highlights',
        admissions: 'Admissions',
        contact: 'Contact',
        langBtn: 'EN',

        // Intro Section
        introTitle: 'STEM Beheira',
        introSubtitle: 'A public STEM high school preparing students for science, technology, engineering, and mathematics careers',
        introWhatTitle: 'What We Are',
        introWhatText: 'STEM Beheira is a government-run secondary school specializing in science and technology education. Students are admitted through national examination and follow an advanced curriculum focused on hands-on learning.',
        introWhyTitle: 'Why We Exist',
        introWhyText: 'Egypt needs skilled scientists, engineers, and innovators to address national challenges and contribute to global progress. This school develops students who can apply scientific knowledge to solve real-world problems.',
        introHowTitle: 'How Students Learn',
        introHowText: 'Through project-based learning in labs and workshops. Students conduct research, build prototypes, code software, and participate in competitions. Learning emphasizes practical application over memorization.',
        introGainTitle: 'What Students Gain',
        introGainText: 'Technical skills, research experience, and scientific thinking. Graduates are prepared for university STEM programs and can access global opportunities including research programs, competitions, and scholarships.',
        introAdmissionsBtn: 'Learn About Admissions',
        introProgramsBtn: 'Explore Opportunities',

        // Homepage
        schoolTagline: 'Build. Test. Share.',
        schoolDesc: 'Hands-on STEM learning in Behaira with labs, coding studios, and competitions that let students design and ship real projects.',
        admissionsBtn: 'Admissions',
        exploreProgramsBtn: 'Explore Programs',
        openHouseTitle: 'Open House',
        openHouseTime: 'Saturday • 10:00 AM • Innovation Lab',
        openHouseItem1: 'Meet student makers',
        openHouseItem2: 'Tour robotics & biotech labs',
        openHouseItem3: 'Try a 15-minute coding sprint',

        globalProgramsEyebrow: 'Global Programs',
        globalProgramsTitle: 'Discover world-class STEM opportunities',
        globalProgramsDesc: 'Explore 100+ programs from elite institutions worldwide, organized by competitiveness level.',

        topTierTitle: 'Top-Tier Programs',
        topTierDesc: 'Elite programs from MIT, Oxford, Cambridge, and other world-leading institutions. Highly selective opportunities for exceptional students.',
        topTierBtn: 'Explore Elite Programs →',
        topTierPrograms: '15 Programs',
        topTierAcceptance: '<10% Acceptance',

        achievableTitle: 'Achievable Programs',
        achievableDesc: 'Competitive programs from top universities like Stanford, Johns Hopkins, and Duke. Within reach with solid preparation.',
        achievableBtn: 'Explore Achievable Programs →',
        achievablePrograms: '35 Programs',
        achievableAcceptance: '10-30% Acceptance',

        accessibleTitle: 'Accessible Programs',
        accessibleDesc: 'Open-enrollment programs and scholarships for all students. Build foundational skills and explore STEM fields at your pace.',
        accessibleBtn: 'Explore Accessible Programs →',
        accessiblePrograms: '50 Programs',
        accessibleAcceptance: 'Open Admission',

        viewAllProgramsBtn: 'View All Programs Hub →',

        highlightsEyebrow: 'Highlights',
        highlightsTitle: 'Students leading the way',

        admissionsEyebrow: 'Admissions',
        admissionsTitle: 'Ready to apply?',
        admissionsDesc: 'Applications open now for Fall 2027. We review academics, curiosity, and maker projects.',
        keyDatesTitle: 'Key dates',
        keyDate1: 'Info session: Feb 10',
        keyDate2: 'Application deadline: Mar 15',
        keyDate3: 'Interviews: Apr 1-10',
        emailAdmissionsBtn: 'Email admissions',
        portfolioWelcome: '<strong>Portfolio welcome:</strong> Share robotics builds, code repos, science fair projects, or design sketches.',
        shadowStudent: '<strong>Shadow a student:</strong> Spend a day in our labs to see if Behaira STEM School is a fit.',

        contactEyebrow: 'Contact',
        contactTitle: 'Ask a question',
        contactDetailsTitle: 'Want details?',
        contactDetailsDesc: 'Head to our contact page to send a note and see recent inquiries.',
        contactPageBtn: 'Contact page',
        visitSchoolTitle: 'Visit Behaira STEM School',
        visitSchoolAddress: 'Behaira STEM School<br>Innovation District, Behaira<br>Saturday Open Labs: 10:00 AM - 1:00 PM',

        // Admissions Page
        admissionsBadge: 'GOVERNMENT-BASED ADMISSIONS',
        admissionsPageTitle: 'Admissions Process',
        admissionsSubtitle: 'Placement to Behaira STEM School is managed by the Egyptian Ministry of Education through the official national examination and assignment system.',
        authorityTitle: 'Authority',
        authorityText1: 'Admissions are controlled by the Ministry of Education.',
        authorityText2: 'Behaira STEM School does not select students independently. All placements are assigned by the government through the official admissions unit.',
        eligibilityTitle: 'Eligibility Requirements',
        requirement1Title: 'Complete Grade 9',
        requirement1Desc: 'Students must successfully complete Grade 9 (Preparatory 3) in an Egyptian public or private school.',
        requirement2Title: 'National Examination',
        requirement2Desc: 'Qualify through the official STEM secondary school entrance examination administered by the Ministry of Education.',
        requirement3Title: 'Government Assignment',
        requirement3Desc: 'Receive placement to Behaira STEM School through the official government admissions and assignment process.',
        processTitle: 'Admissions Process',
        step1Number: 'STEP 1',
        step1Title: 'Register for Exam',
        step1Desc: 'Register through the Ministry of Education portal during the official registration period.',
        step2Number: 'STEP 2',
        step2Title: 'Take National Exam',
        step2Desc: 'Complete the official STEM secondary school entrance examination at designated testing centers.',
        step3Number: 'STEP 3',
        step3Title: 'Await Results',
        step3Desc: 'Results and placement assignments are published by the Ministry of Education through official channels.',
        step4Number: 'STEP 4',
        step4Title: 'Receive Assignment',
        step4Desc: 'Students assigned to Behaira STEM School will be notified and provided enrollment instructions.',
        noticeTitle: 'Important Notice',
        noticeText1: 'Behaira STEM School does not accept direct applications.',
        noticeText2: 'All student placements are determined exclusively by the Egyptian Ministry of Education. The school enrolls only students officially assigned through the government admissions system.',
        noticeText3: 'For official information about STEM school admissions, please contact the Ministry of Education or visit their official portal.',
        enrolledStudentsTitle: 'For Enrolled Students',
        enrolledStudentsDesc: 'Students who have been officially assigned to Behaira STEM School may contact us for enrollment assistance.',
        emailLabel: 'Email',
        locationLabel: 'Location',
        locationValue: 'Behaira Governorate, Egypt',

        // Contact Page
        contactPageEyebrow: 'Contact',
        contactPageHeading: 'Reach Behaira STEM School',
        contactPageDesc: 'Send us a question about programs, admissions, or partnerships.',
        sendMessageTitle: 'Send a message',
        fullNameLabel: 'Full name',
        nameRequired: 'Name is required.',
        emailRequired: 'Valid email required.',
        messageLabel: 'Message',
        messageRequired: 'Please write a message.',
        sendButton: 'Send',
        recentMessagesTitle: 'Recent messages (demo)',
        noMessagesYet: 'No messages yet. Be the first to reach out.',

        // Program Pages Common
        backToHome: '← Back to Home',
        filterProgramsTitle: 'Filter Programs',
        programTypeFilter: 'Program Type',
        research: 'Research',
        summerSchool: 'Summer School',
        competition: 'Competition',
        costFilter: 'Cost',
        free: 'Free',
        paidAidAvailable: 'Paid (Aid Available)',
        durationFilter: 'Duration',
        weeks: 'weeks',
        months: 'months',
        fieldFilter: 'Field',
        resetFilters: 'Reset Filters',
        programsFound: 'programs found',

        // Top-Tier Page
        topTierBadge: '🏆 ELITE',
        topTierPageTitle: 'Top-Tier Programs',
        topTierPageDesc: 'Highly selective programs from the world\'s most prestigious institutions. These opportunities are designed for exceptional students with outstanding academic records, significant STEM achievements, and proven research or competition success.',

        // Achievable Page
        achievableBadge: '⭐ COMPETITIVE',
        achievablePageTitle: 'Achievable Programs',
        achievablePageDesc: 'Competitive programs from top universities. Within reach with solid preparation and a strong academic record. Perfect for dedicated students who want a challenge.',

        // Accessible Page
        accessibleBadge: '✨ OPEN',
        accessiblePageTitle: 'Accessible Programs',
        accessiblePageDesc: 'Open-enrollment programs and scholarships for everyone. Build foundational skills and explore STEM fields at your own pace without the focus on selectivity.',

        // Writing Page
        navHome: 'Home',
        navPrograms: 'Programs',
        navHighlights: 'Highlights',
        navAdmissions: 'Admissions',
        navWriting: 'Writing Guide',
        navContact: 'Contact',
        writingTitle: 'Academic Writing & Essays',
        writingSubtitle: 'Strong English writing is essential for STEM research, university applications, and professional communication. This guide provides practical tools to improve your academic writing, from essay structure to grammar and vocabulary.',
        howToWriteTitle: 'How to Write a Strong Essay',
        step1Title: 'Understand the Question',
        step1Text: 'Read the essay prompt carefully. Identify key words like "analyze," "compare," "evaluate," or "discuss." Make sure you understand what the question is asking before you begin.',
        step2Title: 'Plan Your Ideas',
        step2Text: 'Brainstorm key points. Organize them logically. Decide on your thesis statement—the main argument of your essay. Create a brief outline with main ideas for each paragraph.',
        step3Title: 'Write the Introduction',
        step3Text: 'Start with context or background. Narrow down to your specific topic. End with a clear thesis statement that presents your main argument or position.',
        step4Title: 'Develop Body Paragraphs',
        step4Text: 'Each paragraph should focus on one main idea. Start with a topic sentence. Provide evidence, examples, or analysis. Explain how it supports your thesis. Use linking words to connect ideas.',
        step5Title: 'Write the Conclusion',
        step5Text: 'Summarize your main points without repeating exact sentences. Restate your thesis in a new way. End with a final thought, implication, or call to action.',
        structureTitle: 'Essay Structure',
        introStructureTitle: 'Introduction',
        introStructureDesc: 'Hook the reader, provide context, present your thesis statement',
        bodyStructureTitle: 'Body Paragraphs',
        bodyStructureDesc: 'Each paragraph = one main idea. Topic sentence → Evidence → Analysis → Link to thesis',
        conclusionStructureTitle: 'Conclusion',
        conclusionStructureDesc: 'Summarize main points, restate thesis, provide final insight or implication',
        examplesTitle: 'Examples of the Best Essays in the World',
        examplesIntro: 'Learn from the masters. These essays are considered exemplary for their clarity, argument, structure, and impact.',
        comparisonTitle: 'Strong vs Weak Writing',
        weakIntroTitle: 'Weak Introduction',
        weakIntroNote: 'Problems: Vague, repetitive, announces what the essay will do instead of making an argument.',
        strongIntroTitle: 'Strong Introduction',
        strongIntroNote: 'Why it works: Specific, clear thesis, sets up the argument, no unnecessary phrases.',
        weakParagraphTitle: 'Weak Body Paragraph',
        weakParagraphNote: 'Problems: Short, simplistic sentences. No depth or analysis. No evidence.',
        strongParagraphTitle: 'Strong Body Paragraph',
        strongParagraphNote: 'Why it works: Clear topic sentence, specific evidence with citation, analysis, acknowledges complexity.',
        tipsTitle: 'Practical Writing Tips',
        tip1Title: 'Be Clear, Not Complicated',
        tip1Text: 'Academic writing should be precise, not filled with unnecessary jargon. Use the simplest word that accurately conveys your meaning.',
        tip2Title: 'One Idea Per Paragraph',
        tip2Text: 'Each paragraph should focus on a single main idea. Start with a topic sentence, develop it, and link it back to your thesis.',
        tip3Title: 'Support Claims with Evidence',
        tip3Text: 'Don\'t make unsupported statements. Use data, examples, quotations, or research to back up your arguments.',
        tip4Title: 'Revise and Edit',
        tip4Text: 'Good writing is rewriting. Review your work for clarity, grammar, and structure. Cut unnecessary words. Read it aloud.',
        tip5Title: 'Use Linking Words',
        tip5Text: 'Connect ideas smoothly: "However," "Therefore," "In addition," "For example." This helps your essay flow logically.',
        tip6Title: 'Answer the Question',
        tip6Text: 'Stay focused on the essay prompt. Don\'t include irrelevant information, no matter how interesting it is.',
        punctuationTitle: 'Punctuation Guide',
        grammarTitle: 'Grammar Essentials',
        vocabTitle: 'Important Academic Words & Forms',
        booksTitle: 'Books That Will Make You a Better Writer',
        ieltsTitle: 'IELTS & International Exams',
        websitesTitle: 'Helpful Websites & Online Resources'
    },
    ar: {
        home: 'الرئيسية',
        programs: 'البرامج',
        highlights: 'الإنجازات',
        admissions: 'القبول',
        contact: 'اتصل بنا',
        langBtn: 'ع',

        // Intro Section
        introTitle: 'STEM البحيرة',
        introSubtitle: 'مدرسة ثانوية حكومية متخصصة في العلوم والتكنولوجيا والهندسة والرياضيات لإعداد الطلاب للمستقبل',
        introWhatTitle: 'ما نحن',
        introWhatText: 'STEM البحيرة مدرسة ثانوية حكومية متخصصة في التعليم العلمي والتقني. يتم قبول الطلاب من خلال الامتحان الوطني ويتبعون منهجاً متقدماً يركز على التعلم العملي.',
        introWhyTitle: 'لماذا نوجد',
        introWhyText: 'مصر بحاجة إلى علماء ومهندسين ومبتكرين ماهرين لمواجهة التحديات الوطنية والمساهمة في التقدم العالمي. تطور هذه المدرسة طلاباً قادرين على تطبيق المعرفة العلمية لحل المشكلات الواقعية.',
        introHowTitle: 'كيف يتعلم الطلاب',
        introHowText: 'من خلال التعلم القائم على المشاريع في المختبرات وورش العمل. يجري الطلاب الأبحاث ويبنون النماذج الأولية ويكتبون البرمجيات ويشاركون في المسابقات. يركز التعلم على التطبيق العملي بدلاً من الحفظ.',
        introGainTitle: 'ما يكتسبه الطلاب',
        introGainText: 'مهارات تقنية وخبرة بحثية وتفكير علمي. الخريجون مستعدون لبرامج STEM الجامعية ويمكنهم الوصول إلى الفرص العالمية بما في ذلك برامج الأبحاث والمسابقات والمنح الدراسية.',
        introAdmissionsBtn: 'تعرف على القبول',
        introProgramsBtn: 'استكشف الفرص',

        // Homepage
        schoolTagline: 'ابنِ. اختبر. شارك.',
        schoolDesc: 'تعليم عملي في العلوم والتكنولوجيا والهندسة والرياضيات في البحيرة مع مختبرات واستوديوهات برمجة ومسابقات تتيح للطلاب تصميم وتنفيذ مشاريع حقيقية.',
        admissionsBtn: 'القبول',
        exploreProgramsBtn: 'استكشف البرامج',
        openHouseTitle: 'يوم مفتوح',
        openHouseTime: 'السبت • 10:00 صباحاً • مختبر الابتكار',
        openHouseItem1: 'التقِ بصانعي المشاريع الطلابية',
        openHouseItem2: 'جولة في مختبرات الروبوتات والتكنولوجيا الحيوية',
        openHouseItem3: 'جرب سباق برمجة لمدة 15 دقيقة',

        globalProgramsEyebrow: 'البرامج العالمية',
        globalProgramsTitle: 'اكتشف فرص STEM عالمية المستوى',
        globalProgramsDesc: 'استكشف أكثر من 100 برنامج من مؤسسات النخبة في جميع أنحاء العالم، منظمة حسب مستوى التنافسية.',

        topTierTitle: 'برامج النخبة',
        topTierDesc: 'برامج النخبة من MIT وأكسفورد وكامبريدج والمؤسسات الرائدة الأخرى. فرص انتقائية للغاية للطلاب الاستثنائيين.',
        topTierBtn: 'استكشف برامج النخبة ←',
        topTierPrograms: '15 برنامجاً',
        topTierAcceptance: 'قبول أقل من 10%',

        achievableTitle: 'البرامج القابلة للتحقيق',
        achievableDesc: 'برامج تنافسية من جامعات رفيعة المستوى مثل ستانفورد وجونز هوبكنز ودوك. في متناول اليد مع إعداد جيد.',
        achievableBtn: 'استكشف البرامج القابلة للتحقيق ←',
        achievablePrograms: '35 برنامجاً',
        achievableAcceptance: 'قبول 10-30%',

        accessibleTitle: 'البرامج المتاحة',
        accessibleDesc: 'برامج مفتوحة التسجيل ومنح دراسية لجميع الطلاب. بناء المهارات الأساسية واستكشاف مجالات STEM بوتيرتك الخاصة.',
        accessibleBtn: 'استكشف البرامج المتاحة ←',
        accessiblePrograms: '50 برنامجاً',
        accessibleAcceptance: 'قبول مفتوح',

        viewAllProgramsBtn: 'عرض جميع البرامج ←',

        highlightsEyebrow: 'الإنجازات',
        highlightsTitle: 'الطلاب يقودون الطريق',

        admissionsEyebrow: 'القبول',
        admissionsTitle: 'هل أنت مستعد للتقديم؟',
        admissionsDesc: 'التقديمات مفتوحة الآن لخريف 2027. نراجع الأكاديميات والفضول والمشاريع العملية.',
        keyDatesTitle: 'التواريخ المهمة',
        keyDate1: 'جلسة معلومات: 10 فبراير',
        keyDate2: 'الموعد النهائي للتقديم: 15 مارس',
        keyDate3: 'المقابلات: 1-10 أبريل',
        emailAdmissionsBtn: 'أرسل بريداً للقبول',
        portfolioWelcome: '<strong>الملف الشخصي مرحب به:</strong> شارك بناءات الروبوتات ومستودعات الأكواد ومشاريع معرض العلوم أو رسومات التصميم.',
        shadowStudent: '<strong>تابع طالباً:</strong> اقضِ يوماً في مختبراتنا لترى ما إذا كانت مدرسة البحيرة STEM مناسبة لك.',

        contactEyebrow: 'اتصل بنا',
        contactTitle: 'اطرح سؤالاً',
        contactDetailsTitle: 'تريد التفاصيل؟',
        contactDetailsDesc: 'توجه إلى صفحة الاتصال لإرسال ملاحظة والاطلاع على الاستفسارات الأخيرة.',
        contactPageBtn: 'صفحة الاتصال',
        visitSchoolTitle: 'قم بزيارة مدرسة البحيرة STEM',
        visitSchoolAddress: 'مدرسة البحيرة STEM<br>منطقة الابتكار، البحيرة<br>المختبرات المفتوحة يوم السبت: 10:00 صباحاً - 1:00 مساءً',

        // Admissions Page
        admissionsBadge: 'القبول الحكومي',
        admissionsPageTitle: 'عملية القبول',
        admissionsSubtitle: 'يتم إدارة التنسيب في مدرسة البحيرة STEM من خلال وزارة التربية والتعليم المصرية عبر نظام الفحص والتعيين الوطني الرسمي.',
        authorityTitle: 'السلطة',
        authorityText1: 'القبول تحت سيطرة وزارة التربية والتعليم.',
        authorityText2: 'مدرسة البحيرة STEM لا تختار الطلاب بشكل مستقل. جميع التنسيبات تتم من قبل الحكومة من خلال وحدة القبول الرسمية.',
        eligibilityTitle: 'متطلبات الأهلية',
        requirement1Title: 'إكمال الصف التاسع',
        requirement1Desc: 'يجب على الطلاب إكمال الصف التاسع (الإعدادية الثالثة) بنجاح في مدرسة حكومية أو خاصة مصرية.',
        requirement2Title: 'الامتحان الوطني',
        requirement2Desc: 'التأهل من خلال امتحان القبول الرسمي للمدارس الثانوية STEM الذي تديره وزارة التربية والتعليم.',
        requirement3Title: 'التعيين الحكومي',
        requirement3Desc: 'تلقي التنسيب لمدرسة البحيرة STEM من خلال عملية القبول والتعيين الحكومية الرسمية.',
        processTitle: 'عملية القبول',
        step1Number: 'الخطوة 1',
        step1Title: 'التسجيل للامتحان',
        step1Desc: 'التسجيل من خلال بوابة وزارة التربية والتعليم خلال فترة التسجيل الرسمية.',
        step2Number: 'الخطوة 2',
        step2Title: 'أداء الامتحان الوطني',
        step2Desc: 'إكمال امتحان القبول الرسمي للمدارس الثانوية STEM في مراكز الاختبار المحددة.',
        step3Number: 'الخطوة 3',
        step3Title: 'انتظار النتائج',
        step3Desc: 'يتم نشر النتائج وتعيينات التنسيب من قبل وزارة التربية والتعليم من خلال القنوات الرسمية.',
        step4Number: 'الخطوة 4',
        step4Title: 'استلام التعيين',
        step4Desc: 'سيتم إخطار الطلاب المعينين لمدرسة البحيرة STEM وتزويدهم بتعليمات التسجيل.',
        noticeTitle: 'إشعار مهم',
        noticeText1: 'مدرسة البحيرة STEM لا تقبل الطلبات المباشرة.',
        noticeText2: 'جميع تنسيبات الطلاب يتم تحديدها حصرياً من قبل وزارة التربية والتعليم المصرية. تقوم المدرسة بتسجيل الطلاب المعينين رسمياً فقط من خلال نظام القبول الحكومي.',
        noticeText3: 'للحصول على معلومات رسمية حول قبول مدارس STEM، يرجى الاتصال بوزارة التربية والتعليم أو زيارة بوابتهم الرسمية.',
        enrolledStudentsTitle: 'للطلاب المسجلين',
        enrolledStudentsDesc: 'يمكن للطلاب الذين تم تعيينهم رسمياً لمدرسة البحيرة STEM الاتصال بنا للحصول على المساعدة في التسجيل.',
        emailLabel: 'البريد الإلكتروني',
        locationLabel: 'الموقع',
        locationValue: 'محافظة البحيرة، مصر',

        // Contact Page
        contactPageEyebrow: 'اتصل بنا',
        contactPageHeading: 'تواصل مع مدرسة البحيرة STEM',
        contactPageDesc: 'أرسل لنا سؤالاً حول البرامج أو القبول أو الشراكات.',
        sendMessageTitle: 'إرسال رسالة',
        fullNameLabel: 'الاسم الكامل',
        nameRequired: 'الاسم مطلوب.',
        emailRequired: 'بريد إلكتروني صالح مطلوب.',
        messageLabel: 'الرسالة',
        messageRequired: 'يرجى كتابة رسالة.',
        sendButton: 'إرسال',
        recentMessagesTitle: 'الرسائل الأخيرة (عرض توضيحي)',
        noMessagesYet: 'لا توجد رسائل بعد. كن أول من يتواصل.',

        // Program Pages Common
        backToHome: '← العودة إلى الصفحة الرئيسية',
        filterProgramsTitle: 'تصفية البرامج',
        programTypeFilter: 'نوع البرنامج',
        research: 'بحث',
        summerSchool: 'مدرسة صيفية',
        competition: 'مسابقة',
        costFilter: 'التكلفة',
        free: 'مجاني',
        paidAidAvailable: 'مدفوع (مساعدة متاحة)',
        durationFilter: 'المدة',
        weeks: 'أسابيع',
        months: 'شهور',
        fieldFilter: 'المجال',
        resetFilters: 'إعادة تعيين الفلاتر',
        programsFound: 'برنامج تم العثور عليه',

        // Top-Tier Page
        topTierBadge: '🏆 النخبة',
        topTierPageTitle: 'برامج النخبة',
        topTierPageDesc: 'برامج انتقائية للغاية من أرقى المؤسسات في العالم. هذه الفرص مصممة للطلاب الاستثنائيين ذوي السجلات الأكاديمية المتميزة، والإنجازات الكبيرة في STEM، ونجاح البحث أو المسابقة المثبت.',

        // Achievable Page
        achievableBadge: '⭐ تنافسي',
        achievablePageTitle: 'البرامج القابلة للتحقيق',
        achievablePageDesc: 'برامج تنافسية من أفضل الجامعات. في متناول اليد مع إعداد قوي وسجل أكاديمي قوي. مثالية للطلاب المتفانين الذين يرغبون في التحدي.',

        // Accessible Page
        accessibleBadge: '✨ مفتوح',
        accessiblePageTitle: 'البرامج المتاحة',
        accessiblePageDesc: 'برامج مفتوحة التسجيل ومنح دراسية للجميع. ابنِ المهارات الأساسية واستكشف مجالات STEM بوتيرتك الخاصة دون التركيز على الانتقائية.',

        // Writing Page
        navHome: 'الرئيسية',
        navPrograms: 'البرامج',
        navHighlights: 'الإنجازات',
        navAdmissions: 'القبول',
        navWriting: 'دليل الكتابة',
        navContact: 'اتصل بنا',
        writingTitle: 'الكتابة الأكاديمية والمقالات',
        writingSubtitle: 'الكتابة القوية باللغة الإنجليزية ضرورية للأبحاث العلمية وطلبات الجامعات والتواصل المهني. يوفر هذا الدليل أدوات عملية لتحسين كتابتك الأكاديمية، من بنية المقال إلى القواعد والمفردات.',
        howToWriteTitle: 'كيف تكتب مقالاً قوياً',
        step1Title: 'افهم السؤال',
        step1Text: 'اقرأ موضوع المقال بعناية. حدد الكلمات الرئيسية مثل "حلل" أو "قارن" أو "قيّم" أو "ناقش". تأكد من فهمك لما يطلبه السؤال قبل البدء.',
        step2Title: 'خطط لأفكارك',
        step2Text: 'اعصف ذهنياً بالنقاط الرئيسية. نظمها منطقياً. قرر أطروحتك الرئيسية - الحجة الأساسية لمقالك. أنشئ مخططاً مختصراً بالأفكار الرئيسية لكل فقرة.',
        step3Title: 'اكتب المقدمة',
        step3Text: 'ابدأ بالسياق أو الخلفية. اضيّق نطاق الموضوع المحدد. اختم ببيان أطروحة واضح يقدم حجتك أو موقفك الرئيسي.',
        step4Title: 'طور فقرات الجسم',
        step4Text: 'يجب أن تركز كل فقرة على فكرة رئيسية واحدة. ابدأ بجملة موضوعية. قدم دليلاً أو أمثلة أو تحليلاً. اشرح كيف يدعم أطروحتك. استخدم كلمات الربط لربط الأفكار.',
        step5Title: 'اكتب الخاتمة',
        step5Text: 'لخص نقاطك الرئيسية دون تكرار الجمل الدقيقة. أعد صياغة أطروحتك بطريقة جديدة. اختم بفكرة نهائية أو تأثير أو دعوة للعمل.',
        structureTitle: 'بنية المقال',
        introStructureTitle: 'المقدمة',
        introStructureDesc: 'جذب القارئ، تقديم السياق، عرض بيان الأطروحة',
        bodyStructureTitle: 'فقرات الجسم',
        bodyStructureDesc: 'كل فقرة = فكرة رئيسية واحدة. جملة موضوعية → دليل → تحليل → ربط بالأطروحة',
        conclusionStructureTitle: 'الخاتمة',
        conclusionStructureDesc: 'تلخيص النقاط الرئيسية، إعادة صياغة الأطروحة، تقديم رؤية نهائية أو تأثير',
        examplesTitle: 'أمثلة من أفضل المقالات في العالم',
        examplesIntro: 'تعلم من المعلمين. تعتبر هذه المقالات نموذجية لوضوحها وحجتها وبنيتها وتأثيرها.',
        comparisonTitle: 'الكتابة القوية مقابل الضعيفة',
        weakIntroTitle: 'مقدمة ضعيفة',
        weakIntroNote: 'المشاكل: غامضة، متكررة، تعلن عما سيفعله المقال بدلاً من تقديم حجة.',
        strongIntroTitle: 'مقدمة قوية',
        strongIntroNote: 'لماذا تنجح: محددة، أطروحة واضحة، تضع الحجة، لا عبارات غير ضرورية.',
        weakParagraphTitle: 'فقرة جسم ضعيفة',
        weakParagraphNote: 'المشاكل: جمل قصيرة ومبسطة. لا عمق أو تحليل. لا دليل.',
        strongParagraphTitle: 'فقرة جسم قوية',
        strongParagraphNote: 'لماذا تنجح: جملة موضوعية واضحة، دليل محدد مع اقتباس، تحليل، يعترف بالتعقيد.',
        tipsTitle: 'نصائح كتابية عملية',
        tip1Title: 'كن واضحاً، وليس معقداً',
        tip1Text: 'يجب أن تكون الكتابة الأكاديمية دقيقة، وليست مليئة بالمصطلحات غير الضرورية. استخدم أبسط كلمة تنقل معناك بدقة.',
        tip2Title: 'فكرة واحدة لكل فقرة',
        tip2Text: 'يجب أن تركز كل فقرة على فكرة رئيسية واحدة. ابدأ بجملة موضوعية، طورها، واربطها بأطروحتك.',
        tip3Title: 'ادعم الادعاءات بالأدلة',
        tip3Text: 'لا تقدم بيانات غير مدعومة. استخدم البيانات أو الأمثلة أو الاقتباسات أو الأبحاث لدعم حججك.',
        tip4Title: 'راجع وحرر',
        tip4Text: 'الكتابة الجيدة هي إعادة كتابة. راجع عملك من حيث الوضوح والقواعد والبنية. احذف الكلمات غير الضرورية. اقرأها بصوت عالٍ.',
        tip5Title: 'استخدم كلمات الربط',
        tip5Text: 'اربط الأفكار بسلاسة: "ومع ذلك"، "لذلك"، "بالإضافة إلى ذلك"، "على سبيل المثال". يساعد هذا مقالك على التدفق منطقياً.',
        tip6Title: 'أجب عن السؤال',
        tip6Text: 'ابق مركزاً على موضوع المقال. لا تدرج معلومات غير ذات صلة، مهما كانت مثيرة للاهتمام.',
        punctuationTitle: 'دليل علامات الترقيم',
        grammarTitle: 'أساسيات القواعد',
        vocabTitle: 'كلمات أكاديمية مهمة وأشكالها',
        booksTitle: 'كتب ستجعلك كاتباً أفضل',
        ieltsTitle: 'IELTS والامتحانات الدولية',
        websitesTitle: 'مواقع ويب ومصادر مفيدة عبر الإنترنت'
    }
};

function updateLanguage(lang) {
    const trans = translations[lang];
    const langText = document.querySelector('.lang-text');

    if (langText) {
        langText.textContent = trans.langBtn;
    }

    // Update navigation links
    const navLinks = document.querySelectorAll('.header__link');
    if (navLinks.length >= 5) {
        navLinks[0].textContent = trans.home;
        navLinks[1].textContent = trans.programs;
        navLinks[2].textContent = trans.highlights;
        navLinks[3].textContent = trans.admissions;
        navLinks[4].textContent = trans.contact;
    }

    document.documentElement.setAttribute('lang', lang);
    document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
    localStorage.setItem('language', lang);

    // Update all translatable elements
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (trans[key]) {
            if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                element.placeholder = trans[key];
            } else {
                element.innerHTML = trans[key];
            }
        }
    });
}

// Initialize with saved language
updateLanguage(savedLang);

if (langToggle) {
    langToggle.addEventListener('click', () => {
        const currentLang = document.documentElement.getAttribute('lang');
        const newLang = currentLang === 'en' ? 'ar' : 'en';
        updateLanguage(newLang);
    });
}

// ========================================
// PREMIUM CINEMATIC 3D SPACE BACKGROUND
// ========================================

class PremiumSpaceBackground {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) return;

        this.ctx = this.canvas.getContext('2d');
        this.stars = [];
        this.nebulaClouds = [];
        this.dataStreaks = [];
        this.mouse = { x: 0, y: 0 };
        this.scroll = 0;
        this.time = 0;

        this.init();
    }

    init() {
        this.resize();
        window.addEventListener('resize', () => this.resize());
        window.addEventListener('mousemove', (e) => this.handleMouse(e));
        window.addEventListener('scroll', () => this.handleScroll());

        this.createStars();
        this.createNebulaClouds();
        this.createDataStreaks();
        this.animate();
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        this.centerX = this.canvas.width / 2;
        this.centerY = this.canvas.height / 2;
    }

    handleMouse(e) {
        this.mouse.x = (e.clientX - this.centerX) / this.centerX;
        this.mouse.y = (e.clientY - this.centerY) / this.centerY;
    }

    handleScroll() {
        this.scroll = window.pageYOffset || document.documentElement.scrollTop;
    }

    createStars() {
        const starCount = 800;

        for (let i = 0; i < starCount; i++) {
            this.stars.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                z: Math.random() * 3, // Depth layer (0-3)
                size: Math.random() * 1.5 + 0.3,
                brightness: Math.random() * 0.6 + 0.15, // Reduced brightness for better text contrast
                twinkleSpeed: Math.random() * 0.015 + 0.003,
                twinkleOffset: Math.random() * Math.PI * 2
            });
        }
    }

    createNebulaClouds() {
        const cloudCount = 5;

        for (let i = 0; i < cloudCount; i++) {
            this.nebulaClouds.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                radius: Math.random() * 200 + 150,
                color: Math.random() > 0.5 ? 'rgba(0, 229, 255, 0.02)' : 'rgba(124, 124, 255, 0.015)', // Even more subtle
                drift: {
                    x: (Math.random() - 0.5) * 0.08,
                    y: (Math.random() - 0.5) * 0.08
                }
            });
        }
    }

    createDataStreaks() {
        const streakCount = 4; // Reduced from 6 to minimize distraction

        for (let i = 0; i < streakCount; i++) {
            this.dataStreaks.push({
                x: Math.random() * this.canvas.width,
                y: -50,
                length: Math.random() * 120 + 80,
                speed: Math.random() * 0.25 + 0.12,
                opacity: Math.random() * 0.15 + 0.08, // Reduced opacity
                angle: Math.random() * 0.15 - 0.075
            });
        }
    }

    drawNebulaClouds() {
        this.nebulaClouds.forEach(cloud => {
            const gradient = this.ctx.createRadialGradient(
                cloud.x, cloud.y, 0,
                cloud.x, cloud.y, cloud.radius
            );
            gradient.addColorStop(0, cloud.color);
            gradient.addColorStop(1, 'transparent');

            this.ctx.fillStyle = gradient;
            this.ctx.fillRect(
                cloud.x - cloud.radius,
                cloud.y - cloud.radius,
                cloud.radius * 2,
                cloud.radius * 2
            );

            // Gentle drift
            cloud.x += cloud.drift.x;
            cloud.y += cloud.drift.y;

            // Wrap around
            if (cloud.x < -cloud.radius) cloud.x = this.canvas.width + cloud.radius;
            if (cloud.x > this.canvas.width + cloud.radius) cloud.x = -cloud.radius;
            if (cloud.y < -cloud.radius) cloud.y = this.canvas.height + cloud.radius;
            if (cloud.y > this.canvas.height + cloud.radius) cloud.y = -cloud.radius;
        });
    }

    drawStars() {
        this.stars.forEach(star => {
            // Parallax based on depth
            const parallaxX = this.mouse.x * star.z * 15;
            const parallaxY = this.mouse.y * star.z * 15;
            const scrollEffect = this.scroll * star.z * 0.02;

            const x = star.x + parallaxX;
            const y = star.y + parallaxY - scrollEffect;

            // Twinkling effect
            const twinkle = Math.sin(this.time * star.twinkleSpeed + star.twinkleOffset);
            const alpha = star.brightness * (0.7 + twinkle * 0.3);

            // Color based on depth
            let color;
            if (star.z > 2) {
                color = `rgba(0, 229, 255, ${alpha})`; // Foreground: cyan
            } else if (star.z > 1) {
                color = `rgba(229, 231, 235, ${alpha})`; // Mid: white
            } else {
                color = `rgba(124, 124, 255, ${alpha * 0.6})`; // Deep: violet
            }

            this.ctx.fillStyle = color;
            this.ctx.beginPath();
            this.ctx.arc(x, y, star.size, 0, Math.PI * 2);
            this.ctx.fill();

            // Add subtle glow for bright stars
            if (star.brightness > 0.7 && star.z > 2) {
                this.ctx.fillStyle = `rgba(0, 229, 255, ${alpha * 0.3})`;
                this.ctx.beginPath();
                this.ctx.arc(x, y, star.size * 2, 0, Math.PI * 2);
                this.ctx.fill();
            }
        });
    }

    drawDataStreaks() {
        this.dataStreaks.forEach(streak => {
            const gradient = this.ctx.createLinearGradient(
                streak.x, streak.y,
                streak.x + Math.sin(streak.angle) * 5,
                streak.y + streak.length
            );
            gradient.addColorStop(0, 'transparent');
            gradient.addColorStop(0.5, `rgba(0, 229, 255, ${streak.opacity})`);
            gradient.addColorStop(1, 'transparent');

            this.ctx.strokeStyle = gradient;
            this.ctx.lineWidth = 1;
            this.ctx.beginPath();
            this.ctx.moveTo(streak.x, streak.y);
            this.ctx.lineTo(
                streak.x + Math.sin(streak.angle) * 5,
                streak.y + streak.length
            );
            this.ctx.stroke();

            // Move down slowly
            streak.y += streak.speed;

            // Reset when off screen
            if (streak.y > this.canvas.height + 200) {
                streak.y = -50;
                streak.x = Math.random() * this.canvas.width;
            }
        });
    }

    animate() {
        this.time += 0.016; // ~60fps

        // Darker clear for better text contrast
        this.ctx.fillStyle = 'rgba(10, 16, 32, 0.5)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.drawNebulaClouds();
        this.drawStars();
        this.drawDataStreaks();

        // Add subtle vignette for text readability
        this.drawVignette();

        requestAnimationFrame(() => this.animate());
    }

    drawVignette() {
        const gradient = this.ctx.createRadialGradient(
            this.canvas.width / 2, this.canvas.height / 2, 0,
            this.canvas.width / 2, this.canvas.height / 2, this.canvas.width * 0.7
        );
        gradient.addColorStop(0, 'transparent');
        gradient.addColorStop(0.7, 'rgba(10, 16, 32, 0.3)');
        gradient.addColorStop(1, 'rgba(10, 16, 32, 0.6)');

        this.ctx.fillStyle = gradient;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    }
}

// Initialize space background
new PremiumSpaceBackground('spaceCanvas');

// Minimal scroll lines (subtle data streams)
function initScrollLines() {
    const scrollLinesContainer = document.getElementById('scrollLines');
    if (!scrollLinesContainer) return;

    const lines = [];
    const lineCount = 8;
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;

    for (let i = 0; i < lineCount; i++) {
        const line = document.createElement('div');
        line.className = 'scroll-line';
        line.style.left = (Math.random() * windowWidth) + 'px';
        line.style.height = (Math.random() * 300 + 200) + 'px';
        line.style.top = '-' + (Math.random() * 300 + 100) + 'px';
        scrollLinesContainer.appendChild(line);

        lines.push({
            element: line,
            x: Math.random() * windowWidth,
            y: parseFloat(line.style.top),
            speed: Math.random() * 0.3 + 0.1
        });
    }

    window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        lines.forEach(line => {
            const newY = line.y + (scrollTop * line.speed);
            line.element.style.top = newY + 'px';

            if (newY > windowHeight + 400) {
                line.y = -400;
                line.element.style.left = (Math.random() * windowWidth) + 'px';
            }
        });
    });
}

initScrollLines();

// ========================================
// SECTION & FOOTER FADE-IN ANIMATIONS
// ========================================

// Intersection Observer for sections
const observerOptions = {
    threshold: 0.15,
    rootMargin: '0px 0px -50px 0px'
};

const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Observe all sections
document.querySelectorAll('.section').forEach(section => {
    sectionObserver.observe(section);
});

// Footer fade-in observer
const footer = document.getElementById('mainFooter');
if (footer) {
    const footerObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.2 });

    footerObserver.observe(footer);
}

// ========================================
// FALLING STARS ANIMATION
// ========================================

class FallingStars {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) return;

        this.ctx = this.canvas.getContext('2d');
        this.stars = [];
        this.maxStars = 8; // Limited quantity
        this.init();
    }

    init() {
        this.resize();
        window.addEventListener('resize', () => this.resize());
        this.createStars();
        this.animate();
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    createStars() {
        // Create initial stars with random delays
        for (let i = 0; i < this.maxStars; i++) {
            setTimeout(() => {
                this.addStar();
            }, Math.random() * 8000);
        }
    }

    addStar() {
        this.stars.push({
            x: Math.random() * this.canvas.width,
            y: -50,
            size: Math.random() * 1.5 + 0.8,
            speed: Math.random() * 0.3 + 0.15, // Very slow
            opacity: Math.random() * 0.4 + 0.2, // Low opacity
            angle: Math.random() * 15 - 7.5, // Slight diagonal movement
            glow: Math.random() * 3 + 2,
            life: 0,
            maxLife: 1
        });
    }

    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // Update and draw stars
        for (let i = this.stars.length - 1; i >= 0; i--) {
            const star = this.stars[i];

            // Update position
            star.y += star.speed;
            star.x += Math.sin(star.angle) * 0.2;
            star.life += 0.002;

            // Calculate opacity fade
            let opacity = star.opacity;
            if (star.life < 0.1) {
                opacity *= star.life / 0.1; // Fade in
            } else if (star.life > 0.9) {
                opacity *= (1 - star.life) / 0.1; // Fade out
            }

            // Draw star with glow
            const gradient = this.ctx.createRadialGradient(
                star.x, star.y, 0,
                star.x, star.y, star.glow * 3
            );
            gradient.addColorStop(0, `rgba(255, 255, 255, ${opacity})`);
            gradient.addColorStop(0.3, `rgba(0, 229, 255, ${opacity * 0.6})`);
            gradient.addColorStop(1, 'rgba(0, 229, 255, 0)');

            this.ctx.fillStyle = gradient;
            this.ctx.beginPath();
            this.ctx.arc(star.x, star.y, star.glow, 0, Math.PI * 2);
            this.ctx.fill();

            // Core star
            this.ctx.fillStyle = `rgba(255, 255, 255, ${opacity})`;
            this.ctx.beginPath();
            this.ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
            this.ctx.fill();

            // Remove stars that are off screen or life expired
            if (star.y > this.canvas.height + 50 || star.life >= star.maxLife) {
                this.stars.splice(i, 1);

                // Add new star after random delay
                setTimeout(() => {
                    if (this.stars.length < this.maxStars) {
                        this.addStar();
                    }
                }, Math.random() * 10000 + 5000);
            }
        }

        requestAnimationFrame(() => this.animate());
    }
}

// Initialize falling stars (respect reduced motion)
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    new FallingStars('fallingStarsCanvas');
}

// ========================================
// "YOUR NAME" ANIME-INSPIRED 3D DEPTH PARTICLES
// ========================================

class YourNameDepthParticles {
    constructor() {
        // Create dedicated canvas for depth particles
        this.canvas = document.createElement('canvas');
        this.canvas.id = 'depthParticlesCanvas';
        this.canvas.style.position = 'fixed';
        this.canvas.style.top = '0';
        this.canvas.style.left = '0';
        this.canvas.style.width = '100%';
        this.canvas.style.height = '100%';
        this.canvas.style.zIndex = '1';
        this.canvas.style.pointerEvents = 'none';
        this.canvas.style.opacity = '0.4';
        document.body.prepend(this.canvas);

        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.scroll = 0;
        this.mouse = { x: 0, y: 0 };

        this.init();
    }

    init() {
        this.resize();
        window.addEventListener('resize', () => this.resize());
        window.addEventListener('scroll', () => {
            this.scroll = window.pageYOffset;
        });
        window.addEventListener('mousemove', (e) => {
            this.mouse.x = e.clientX;
            this.mouse.y = e.clientY;
        });

        this.createParticles();
        this.animate();
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    createParticles() {
        const particleCount = 60; // Moderate amount

        for (let i = 0; i < particleCount; i++) {
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height * 2, // Spread vertically
                z: Math.random() * 5 + 0.3, // Depth layer (0.3-5.3)
                size: Math.random() * 3 + 1,
                baseSpeed: Math.random() * 0.5 + 0.2,
                opacity: Math.random() * 0.6 + 0.2,
                color: this.getParticleColor(),
                oscillation: Math.random() * Math.PI * 2,
                oscillationSpeed: Math.random() * 0.02 + 0.01,
                horizontalDrift: (Math.random() - 0.5) * 0.3
            });
        }
    }

    getParticleColor() {
        const colors = [
            { r: 0, g: 229, b: 255 }, // Cyan
            { r: 124, g: 124, b: 255 }, // Violet
            { r: 255, g: 255, b: 255 }, // White
            { r: 100, g: 200, b: 255 } // Light blue
        ];
        return colors[Math.floor(Math.random() * colors.length)];
    }

    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // Sort particles by z-index for proper depth
        this.particles.sort((a, b) => a.z - b.z);

        for (let particle of this.particles) {
            // Parallax based on depth (z-index)
            const parallaxX = (this.mouse.x - this.canvas.width / 2) * (particle.z * 0.01);
            const parallaxY = (this.mouse.y - this.canvas.height / 2) * (particle.z * 0.01);

            // Scroll-based movement (falling down as you scroll)
            const scrollEffect = this.scroll * particle.z * 0.05;

            // Oscillation for dreamy floating effect
            particle.oscillation += particle.oscillationSpeed;
            const oscillationX = Math.sin(particle.oscillation) * 10 * particle.z;

            // Update position
            particle.y += particle.baseSpeed * particle.z;
            particle.x += particle.horizontalDrift * particle.z;

            // Calculate final position with all effects
            const finalX = particle.x + parallaxX + oscillationX;
            const finalY = particle.y - scrollEffect + parallaxY;

            // Scale based on depth
            const scale = particle.z / 5;
            const size = particle.size * scale;

            // Opacity based on depth (farther = more transparent)
            const depthOpacity = particle.opacity * (0.3 + (particle.z / 5) * 0.7);

            // Draw particle with glow
            const gradient = this.ctx.createRadialGradient(
                finalX, finalY, 0,
                finalX, finalY, size * 3
            );
            gradient.addColorStop(0, `rgba(${particle.color.r}, ${particle.color.g}, ${particle.color.b}, ${depthOpacity})`);
            gradient.addColorStop(0.5, `rgba(${particle.color.r}, ${particle.color.g}, ${particle.color.b}, ${depthOpacity * 0.5})`);
            gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');

            this.ctx.fillStyle = gradient;
            this.ctx.beginPath();
            this.ctx.arc(finalX, finalY, size * 3, 0, Math.PI * 2);
            this.ctx.fill();

            // Draw core particle
            this.ctx.fillStyle = `rgba(${particle.color.r}, ${particle.color.g}, ${particle.color.b}, ${depthOpacity})`;
            this.ctx.beginPath();
            this.ctx.arc(finalX, finalY, size, 0, Math.PI * 2);
            this.ctx.fill();

            // Wrap around screen
            if (particle.y - scrollEffect > this.canvas.height + 100) {
                particle.y = -100;
                particle.x = Math.random() * this.canvas.width;
            }
            if (particle.x < -50) particle.x = this.canvas.width + 50;
            if (particle.x > this.canvas.width + 50) particle.x = -50;
        }

        requestAnimationFrame(() => this.animate());
    }
}

// Initialize "Your Name" depth particles (respect reduced motion)
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    new YourNameDepthParticles();
}

// ========================================
// FASTER FALLING ASTEROIDS ("YOUR NAME" STYLE)
// ========================================

class FallingAsteroids {
    constructor() {
        // Create dedicated canvas for asteroids
        this.canvas = document.createElement('canvas');
        this.canvas.id = 'fallingAsteroidsCanvas';
        this.canvas.style.position = 'fixed';
        this.canvas.style.top = '0';
        this.canvas.style.left = '0';
        this.canvas.style.width = '100%';
        this.canvas.style.height = '100%';
        this.canvas.style.zIndex = '1';
        this.canvas.style.pointerEvents = 'none';
        this.canvas.style.opacity = '0.5';
        document.body.prepend(this.canvas);

        this.ctx = this.canvas.getContext('2d');
        this.asteroids = [];
        this.scroll = 0;

        this.init();
    }

    init() {
        this.resize();
        window.addEventListener('resize', () => this.resize());
        window.addEventListener('scroll', () => {
            this.scroll = window.pageYOffset;
        });

        this.createAsteroids();
        this.animate();
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    createAsteroids() {
        const asteroidCount = 25; // Moderate amount

        for (let i = 0; i < asteroidCount; i++) {
            this.addAsteroid();
        }
    }

    addAsteroid() {
        this.asteroids.push({
            x: Math.random() * this.canvas.width,
            y: Math.random() * -this.canvas.height - 100,
            z: Math.random() * 3 + 0.5, // Depth layer
            size: Math.random() * 8 + 3,
            speed: Math.random() * 4 + 2, // FASTER: 2-6 pixels per frame
            rotation: Math.random() * Math.PI * 2,
            rotationSpeed: (Math.random() - 0.5) * 0.08,
            horizontalDrift: (Math.random() - 0.5) * 0.8,
            opacity: Math.random() * 0.5 + 0.3,
            shape: Math.floor(Math.random() * 3), // 3 different shapes
            trail: []
        });
    }

    drawAsteroid(asteroid) {
        const scale = asteroid.z / 3;
        const size = asteroid.size * scale;

        this.ctx.save();
        this.ctx.translate(asteroid.x, asteroid.y);
        this.ctx.rotate(asteroid.rotation);

        // Different asteroid shapes
        this.ctx.fillStyle = `rgba(150, 180, 255, ${asteroid.opacity})`;
        this.ctx.strokeStyle = `rgba(0, 229, 255, ${asteroid.opacity * 0.6})`;
        this.ctx.lineWidth = 1;

        if (asteroid.shape === 0) {
            // Irregular rock shape
            this.ctx.beginPath();
            for (let i = 0; i < 6; i++) {
                const angle = (i / 6) * Math.PI * 2;
                const radius = size * (0.8 + Math.random() * 0.4);
                const x = Math.cos(angle) * radius;
                const y = Math.sin(angle) * radius;
                if (i === 0) this.ctx.moveTo(x, y);
                else this.ctx.lineTo(x, y);
            }
            this.ctx.closePath();
            this.ctx.fill();
            this.ctx.stroke();
        } else if (asteroid.shape === 1) {
            // Pentagon shape
            this.ctx.beginPath();
            for (let i = 0; i < 5; i++) {
                const angle = (i / 5) * Math.PI * 2 - Math.PI / 2;
                const x = Math.cos(angle) * size;
                const y = Math.sin(angle) * size;
                if (i === 0) this.ctx.moveTo(x, y);
                else this.ctx.lineTo(x, y);
            }
            this.ctx.closePath();
            this.ctx.fill();
            this.ctx.stroke();
        } else {
            // Diamond shape
            this.ctx.beginPath();
            this.ctx.moveTo(0, -size);
            this.ctx.lineTo(size * 0.7, 0);
            this.ctx.lineTo(0, size);
            this.ctx.lineTo(-size * 0.7, 0);
            this.ctx.closePath();
            this.ctx.fill();
            this.ctx.stroke();
        }

        // Add glow
        const gradient = this.ctx.createRadialGradient(0, 0, 0, 0, 0, size * 2);
        gradient.addColorStop(0, `rgba(0, 229, 255, ${asteroid.opacity * 0.3})`);
        gradient.addColorStop(1, 'transparent');
        this.ctx.fillStyle = gradient;
        this.ctx.beginPath();
        this.ctx.arc(0, 0, size * 2, 0, Math.PI * 2);
        this.ctx.fill();

        this.ctx.restore();
    }

    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        for (let i = this.asteroids.length - 1; i >= 0; i--) {
            const asteroid = this.asteroids[i];

            // Fast falling motion
            asteroid.y += asteroid.speed * asteroid.z;
            asteroid.x += asteroid.horizontalDrift * asteroid.z;
            asteroid.rotation += asteroid.rotationSpeed;

            // Scroll effect (even faster when scrolling)
            const scrollEffect = this.scroll * 0.02 * asteroid.z;

            this.drawAsteroid(asteroid);

            // Remove and replace asteroids that are off screen
            if (asteroid.y - scrollEffect > this.canvas.height + 50) {
                this.asteroids.splice(i, 1);
                this.addAsteroid();
            }
            if (asteroid.x < -50) asteroid.x = this.canvas.width + 50;
            if (asteroid.x > this.canvas.width + 50) asteroid.x = -50;
        }

        requestAnimationFrame(() => this.animate());
    }
}

// Initialize falling asteroids (respect reduced motion)
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    new FallingAsteroids();
}

// 3D Mouse tracking for hero banner
const heroBanner = document.getElementById('heroBanner');
const heroContent = document.getElementById('heroContent');
const heroCard = document.getElementById('heroCard');

if (heroBanner && heroContent && heroCard) {
    document.addEventListener('mousemove', (e) => {
        const rect = heroBanner.getBoundingClientRect();
        if (rect.bottom < 0 || rect.top > window.innerHeight) return;

        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = (y - centerY) / 20;
        const rotateY = (centerX - x) / 20;

        const contentDistance = 40;
        const cardDistance = 35;

        heroContent.style.transform = `perspective(1200px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(${contentDistance}px)`;
        heroCard.style.transform = `perspective(1200px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(${cardDistance}px)`;
    });

    heroBanner.addEventListener('mouseleave', () => {
        heroContent.style.transform = 'perspective(1200px) rotateX(0) rotateY(0) translateZ(0)';
        heroCard.style.transform = 'perspective(1200px) rotateX(0) rotateY(0) translateZ(0)';
    });
}

// Smooth scroll for in-page links
const links = document.querySelectorAll('a[href^="#"]');
links.forEach((link) => {
    link.addEventListener('click', (event) => {
        const targetId = link.getAttribute('href');
        if (!targetId || targetId === '#') return;
        const target = document.querySelector(targetId);
        if (target) {
            event.preventDefault();
            target.scrollIntoView({ behavior: 'smooth' });
            nav.classList.remove('nav--open');
        }
    });
});

// Bootstrap-like validation for contact form
const forms = document.querySelectorAll('.needs-validation');
forms.forEach((form) => {
    form.addEventListener('submit', (event) => {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        form.classList.add('was-validated');
    }, false);
});

// ========================================
// INTRO CANVAS ANIMATION
// ========================================

const introCanvas = document.getElementById('introCanvas');
if (introCanvas) {
    const introCtx = introCanvas.getContext('2d');
    let introWidth = introCanvas.width = window.innerWidth;
    let introHeight = introCanvas.height = window.innerHeight;

    // Falling stars for intro
    const introStars = [];
    const introStarCount = 80;

    class IntroStar {
        constructor() {
            this.reset();
        }

        reset() {
            this.x = Math.random() * introWidth;
            this.y = Math.random() * -introHeight;
            this.speed = Math.random() * 1.5 + 0.5;
            this.size = Math.random() * 1.5 + 0.5;
            this.opacity = Math.random() * 0.5 + 0.3;
        }

        update() {
            this.y += this.speed;
            if (this.y > introHeight) {
                this.reset();
            }
        }

        draw() {
            introCtx.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
            introCtx.beginPath();
            introCtx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            introCtx.fill();

            // Add glow
            const gradient = introCtx.createRadialGradient(this.x, this.y, 0, this.x, this.y, this.size * 3);
            gradient.addColorStop(0, `rgba(0, 229, 255, ${this.opacity * 0.5})`);
            gradient.addColorStop(1, 'transparent');
            introCtx.fillStyle = gradient;
            introCtx.beginPath();
            introCtx.arc(this.x, this.y, this.size * 3, 0, Math.PI * 2);
            introCtx.fill();
        }
    }

    // Initialize stars
    for (let i = 0; i < introStarCount; i++) {
        introStars.push(new IntroStar());
    }

    function animateIntro() {
        introCtx.clearRect(0, 0, introWidth, introHeight);

        // Draw and update stars
        introStars.forEach(star => {
            star.update();
            star.draw();
        });

        requestAnimationFrame(animateIntro);
    }

    animateIntro();

    // Handle resize
    window.addEventListener('resize', () => {
        introWidth = introCanvas.width = window.innerWidth;
        introHeight = introCanvas.height = window.innerHeight;
    });
}

// ========================================
// STEM Guide Assistant (rule-based helper)
// ========================================

(function initAssistant() {
    const root = document.getElementById('aiAssistant');
    const toggle = document.getElementById('assistantToggle');
    const panel = document.getElementById('assistantPanel');
    const closeBtn = document.getElementById('assistantClose');
    const conversation = document.getElementById('assistantConversation');
    const input = document.getElementById('assistantInput');
    const sendBtn = document.getElementById('assistantSend');
    const quickWrap = document.getElementById('assistantQuick');
    const eyes = document.querySelectorAll('.robot__eye');

    if (!root || !toggle || !panel || !conversation || !input || !sendBtn) return;

    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const links = {
        programs: '/programs',
        top: '/programs/top_tier',
        achievable: '/programs/achievable',
        accessible: '/programs/accessible',
        admissions: '/admissions',
        writingBasics: '/writing/basics',
        writingExamples: '/writing/examples',
        writingResources: '/writing/resources',
        contact: '/contact'
    };

    function addMessage(role, text) {
        const bubble = document.createElement('div');
        bubble.className = `assistant-message assistant-message--${role}`;
        bubble.innerHTML = text;
        conversation.appendChild(bubble);
        conversation.scrollTop = conversation.scrollHeight;
    }

    function safeNavLink(href, label) {
        return `<a href="${href}" class="assistant-link" target="_self">${label}</a>`;
    }

    // ====== ADVANCED ASSISTANT SYSTEM ======
    // Intelligent, context-aware, adaptive behavior
    // Session-based learning and response depth adjustment

    const sessionState = {
        conversationHistory: [],
        exploredTopics: new Set(),
        clarifyingAttempts: 0,
        userUnderstandingLevel: 'beginner'
    };

    function recordTopic(topic) {
        sessionState.exploredTopics.add(topic);
    }

    function getTopicHistory() {
        return Array.from(sessionState.exploredTopics);
    }

    function getLastUserQuestion() {
        const userMessages = sessionState.conversationHistory.filter(m => m.role === 'user');
        return userMessages.length > 0 ? userMessages[userMessages.length - 1].text.toLowerCase() : '';
    }

    function inferContextualCategory(q, previousTopics) {
        // Advanced inference: use context to disambiguate vague questions
        const lastTopics = Array.from(previousTopics);

        // If vague question, use recent context
        if ((q.includes('it') || q.includes('that') || q.includes('it all')) && lastTopics.length > 0) {
            return lastTopics[lastTopics.length - 1];
        }

        // If asking about "getting in", connect to programs if programs were discussed
        if ((q.includes('get in') || q.includes('join') || q.includes('enter')) && previousTopics.has('programs')) {
            return 'admissions';
        }

        // If asking about money/funding after programs discussion
        if ((q.includes('pay') || q.includes('afford') || q.includes('costs')) && previousTopics.has('programs')) {
            return 'scholarships';
        }

        return null; // Use default category detection if inference fails
    }

    function detectIntentAndType(q, previousTopics = new Set()) {
        // Advanced natural language understanding (ChatGPT-like reasoning)
        let category = 'general';
        let questionType = 'info';
        let hasUncertainty = q.includes('?') && q.split('?').length < 3; // Single question, not multiple
        let isVague = q.length < 20 || (q.includes('it') && !q.includes('write')); // Short or vague pronoun use

        // ===== CATEGORY DETECTION (Semantic Understanding) =====

        // Check for contextual inference first (handles vague questions)
        const contextCategory = inferContextualCategory(q, previousTopics);
        if (contextCategory) {
            category = contextCategory;
        }
        // Primary keywords
        else if (q.match(/\b(program|opportunity|summer|stem|ai|course|experience)\b/)) {
            category = 'programs';
        } else if (q.match(/\b(scholarship|financial|fund|money|aid|pay|afford|cost)\b/)) {
            category = 'scholarships';
        } else if (q.match(/\b(admission|apply|exam|eligible|get in|join|enter|apply)\b/)) {
            category = 'admissions';
        } else if (q.match(/\b(writing|essay|english|grammar|improve|paper|article|draft|thesis)\b/)) {
            category = 'writing';
        } else if (q.match(/\b(help|lost|where|lost|navigate|confused|don't know where|how do i find)\b/)) {
            category = 'navigation';
        } else if (q.match(/\b(you|robot|assistant|can you|are you|what can you)\b/)) {
            category = 'about_robot';
        }

        // ===== QUESTION TYPE DETECTION (Intent Understanding) =====

        // Guidance: asking for reasoning, explanation, or understanding
        if (q.match(/\b(why|how|explain|understand|reason|works|process|mechanism)\b/)) {
            questionType = 'guidance';
        }
        // Decision: asking for recommendation or choice
        else if (q.match(/\b(should|recommend|best|which|pick|choose|start with|go with)\b/) ||
            (q.includes('?') && q.includes('or'))) { // "X or Y?" = decision
            questionType = 'decision';
        }
        // Clarification: expressing confusion or asking for simplification
        else if (q.match(/\b(confused|unclear|don't understand|lost|simple|just|basically)\b/) ||
            (isVague && hasUncertainty)) {
            questionType = 'clarification';
        }
        // Followup: continuing from previous message
        else if (getLastUserQuestion() && getLastUserQuestion() !== q &&
            !q.match(/^(so|then|but|what|why|how|can)\s+(you|i|do|about)/i)) {
            // Not just starting a new topic, but building on previous
            questionType = 'followup';
        }
        // Open exploration: asking for overview or what's available
        else if (q.match(/\b(tell me about|what is|what are|any|all|overview|summary)\b/)) {
            questionType = 'info';
        }

        return { category, questionType, hasUncertainty, isVague };
    }

    function buildContextualResponse(category, questionType, q, depth = 'short') {
        // Adapt response based on question type and conversation history
        const topicHistory = getTopicHistory();
        const hasContext = topicHistory.length > 0;

        if (questionType === 'guidance') {
            // User wants to understand something deeper
            return buildGuidanceResponse(category, q, hasContext);
        } else if (questionType === 'decision') {
            // User wants advice or recommendation
            return buildDecisionResponse(category, q, hasContext);
        } else if (questionType === 'clarification') {
            // User is confused, simplify and adjust
            return buildClarificationResponse(category, q);
        } else if (questionType === 'followup') {
            // Build on previous answer, avoid repetition
            return buildFollowupResponse(category, q, topicHistory);
        } else {
            // Standard information
            return buildInformationResponse(category, q, hasContext);
        }
    }

    function buildGuidanceResponse(category, q, hasContext) {
        // Explain reasoning, show how to think about it
        const responses = {
            programs: {
                answer: 'Here\'s how to think about programs.',
                explain: `All programs teach something valuable—there\'s no "wrong" choice at any level. But they fit different students at different stages. Top-Tier programs (MIT, Stanford) attract exceptional students globally—super rigorous, lots of competition. Achievable programs come from respected universities—challenging but reachable with solid prep. Accessible programs are entry points—they teach fundamentals and build confidence. Think of it like a training ladder: you pick where to climb based on where you are now. Most students start lower and work up as they gain experience. That\'s actually the smartest strategy.`,
                next: `Your first step: ${safeNavLink(links.accessible, 'explore accessible programs')} to understand what\'s out there. Then decide where to reach next.`
            },
            writing: {
                answer: 'Writing is completely learnable—I promise it\'s not magic.',
                explain: `All strong essays follow the same basic pattern: you start by telling people what you\'re going to argue (intro with thesis), then you prove it with examples and explanation (body), and finally you reflect on what it all means (conclusion). That\'s it. The professionals aren\'t doing anything different—they just do it better through practice. The secret is: read examples → notice the pattern → write your own → compare → adjust → repeat. Every professional you\'ve ever read went through that same process.`,
                next: `Start here: ${safeNavLink(links.writingBasics, 'see the structure guide')}, then ${safeNavLink(links.writingExamples, 'study real examples')} to see the pattern.`
            },
            scholarships: {
                answer: 'Scholarships exist in three main flavors—let me break it down.',
                explain: `Merit scholarships reward your achievements (grades, test scores, awards). Need-based scholarships help students whose families need financial support. Program scholarships are specific (for STEM fields, certain schools, certain demographics). The thing is: most competitive programs include some form of funding, because they want to attract diverse, talented students. You don\'t usually choose between program AND scholarship—they often come together.`,
                next: `Browse ${safeNavLink(links.programs, 'programs')} and notice which ones mention funding. That\'s usually a good sign.`
            },
            admissions: {
                answer: 'The admissions process for STEM Beheira is actually straightforward—no hidden secrets.',
                explain: `The Ministry of Education runs a national exam that\'s the same for all STEM schools in Egypt. Here\'s the real path: you finish Grade 9, register for the exam, study (or don\'t, but results show), take the test, and the Ministry publishes results. Placement is based on your score and availability. It\'s completely transparent—no special connections, no politics. That\'s actually an advantage: the system is fair and you can predict outcomes.`,
                next: `For the exact timeline and registration steps, ${safeNavLink(links.admissions, 'check the admissions page')}.`
            },
            navigation: {
                answer: 'Let me help you orient.',
                explain: `This site has four main sections. ${safeNavLink(links.programs, 'Programs')} are organized by difficulty (Accessible → Achievable → Top-Tier). ${safeNavLink(links.writingBasics, 'Writing')} teaches structure, shows examples, and links to tools. ${safeNavLink(links.admissions, 'Admissions')} explains the Ministry process. ${safeNavLink(links.contact, 'Contact us')} if you have questions. Most students start with Programs or Writing, then explore based on interests.`,
                next: `What draws you in first? Programs to explore? Writing to sharpen? Or something else?`
            },
            default: {
                answer: 'Here\'s how to think about this.',
                explain: 'The underlying principle is that there\'s usually more than one way forward—my job is to help you see the options and think through what makes sense for you.',
                next: 'Tell me more about what you\'re exploring, and I can guide you better.'
            }
        };

        const resp = responses[category] || responses.default;
        return `${resp.answer} ${resp.explain} ${resp.next}`;
    }

    function buildDecisionResponse(category, q, hasContext) {
        // Give options, never one "right" answer
        const responses = {
            programs: {
                answer: 'The honest answer: there\'s no "best" program—it\'s what fits YOU.',
                explain: `Start with three real questions. 1) Where are you now academically? (That tells you accessible vs. achievable vs. top-tier.) 2) How much time and energy can you invest in prep? (Tougher programs need more work.) 3) What kind of learning experience appeals to you? (Research? Summer immersion? Competition? Mentorship?) Your answers shape which programs are smart for you to pursue. Also important: it\'s not a one-shot decision. Most successful students start accessible, build skills, then reach higher. That\'s the winning strategy.`,
                next: `Start exploring: ${safeNavLink(links.accessible, 'accessible programs')} (good foundation), then ${safeNavLink(links.achievable, 'achievable')} (stretch), then ${safeNavLink(links.programs, 'top-tier')} (dream big).`
            },
            writing: {
                answer: 'The best writing improvement comes from doing and getting feedback.',
                explain: `Here\'s the actual process that works: 1) Read examples of what you want to write. 2) Notice the structure and style. 3) Write your own version. 4) Compare yours to the examples. 5) Fix the differences. 6) Repeat with new topics. That cycle is more effective than any rule or trick. Every writer you admire went through this same process—thousands of times.`,
                next: `${safeNavLink(links.writingBasics, 'Start with our structure guide')}, then pick an example to study closely, then try writing on the same topic.`
            },
            scholarships: {
                answer: 'Your scholarship strategy depends on your situation.',
                explain: `If you have strong academics → search merit scholarships and ${safeNavLink(links.programs, 'competitive programs')} (they fight for talented students). If finances matter → look for need-based funding and programs known for aid. If you\'re early → explore and see what\'s offered. Here\'s the key insight: most students get funding through their PROGRAM choice, not separate scholarship hunts. Pick a good program first, then check what aid it includes.`,
                next: `Browse ${safeNavLink(links.programs, 'programs by level')} and note which mention funding. That\'s your starting point.`
            },
            admissions: {
                answer: 'For admissions, follow the official path—it\'s the same for everyone.',
                explain: `Complete Grade 9 → Register for the Ministry exam → Study (yes, study helps) → Take the official STEM test → Wait for Ministry placement. Everyone does this. There\'s no shortcut, but there\'s also no political factor. Your score determines your options. If you\'re strategic about exam prep, you improve your outcome. The system is fair; your effort matters.`,
                next: `${safeNavLink(links.admissions, 'Get the exact timeline and registration details here')}.`
            },
            navigation: {
                answer: 'Your choice depends on what you need right now.',
                explain: `Exploring opportunities? Start ${safeNavLink(links.programs, 'here')}. Want to strengthen writing? Go ${safeNavLink(links.writingBasics, 'here')}. Have a specific question? Try searching the site or asking me directly.`,
                next: `What sounds most useful?`
            },
            default: {
                answer: 'There are usually multiple good options.',
                explain: 'What matters most is matching the choice to your current situation and goals.',
                next: 'Tell me more about what you\'re trying to decide, and I can help you see the tradeoffs.'
            }
        };

        const resp = responses[category] || responses.default;
        return `${resp.answer} ${resp.explain} ${resp.next}`;
    }

    function buildClarificationResponse(category, q) {
        // Simplify, use different examples, be more explicit—and feel conversational
        const responses = {
            programs: `Think of programs on a skill ladder. Top-Tier programs (like MIT) are at the top—few spots, require exceptional prep. Achievable programs are in the middle—challenging but doable if you work for it. Accessible programs are lower rungs—easier entry, still valuable learning. You don't start at the top. You pick a rung based on where you are NOW, build skills, then reach higher. Smart students start where they're confident, not where they're drowning. Does that help clarify?`,
            writing: `Here's the real process: 1) Read something well-written (notice what works). 2) Understand why it works (structure, examples, clarity). 3) Write your own (practice). 4) Compare yours to the original (spot differences). 5) Rewrite (apply what you learned). Repeat that loop. It's not about following rules—it's about absorbing patterns by doing. That's how professionals do it.`,
            scholarships: `Money for education comes in three main ways. Merit scholarships say "you earned this"—they're tied to your grades or test scores. Need-based scholarships say "let us help"—they consider your family's financial situation. Program scholarships are built into specific programs—you get them automatically when you join. Most competitive STEM programs include funding, so don't stress about finding scholarships separately. You find the right program, funding often comes with it.`,
            admissions: `Here's the no-nonsense version: The Ministry of Education runs a test. That's it. You register → you study (or don't) → you take the exam → they score it → they assign you to a school based on your score and availability. It's transparent, fair, and the same process for everyone. No secret connections. No politics. Your score matters. Your effort matters. That's actually good news—it means the system is fair.`,
            default: `I might be missing something here. Let me ask differently: what exactly are you trying to figure out? Are we talking about programs? Writing? Getting funding? The admissions process? Once I know, I can explain it more clearly.`
        };

        return responses[category] || responses.default;
    }

    function buildFollowupResponse(category, q, topicHistory) {
        // Reference previous answers, avoid repetition, go deeper—feel like continuing a real conversation
        const contextPhrase = topicHistory.length > 1 ?
            `So following up on what we talked about, ` :
            `Since you just asked about this, `;

        const responses = {
            programs: contextPhrase + `here's the practical thing: when you explore programs, look at what the requirements actually are. That tells you what they value (grades? test scores? experience? leadership?). If you match those requirements reasonably well, that program is a good fit for you. Start with programs where you're close to the requirements, build confidence, then reach higher.`,

            writing: contextPhrase + `remember the structure we talked about applies to every type of writing. What changes is your topic and how deep you go. The key move is: after you write something, compare it to good examples on the same topic. That comparison is where learning happens. You start spotting patterns you can repeat.`,

            scholarships: contextPhrase + `keep in mind that funding isn't separate from programs—it's usually built into the program. When you find a program that excites you, check if it mentions scholarships or financial aid. Most competitive programs do. That's actually how they attract talented students like you.`,

            admissions: contextPhrase + `the registration and exam prep are where you can actually make a difference. The Ministry process is the same for everyone—there's no way to game it. But studying for the exam, understanding what they're testing, managing test day stress—that's all in your control. That's where effort translates to results.`,

            navigation: contextPhrase + `think about what makes sense as your next step. If you just looked at programs, dive deeper into one or ${safeNavLink(links.writingBasics, 'explore writing')}. If you worked on writing, consider how it connects to your program interests. The site is designed for browsing and discovery—there's no wrong path.`,

            default: contextPhrase + `is there a more specific angle on this topic you want to explore? Or does your question lead somewhere else now?`
        };

        return responses[category] || responses.default;
    }

    function buildInformationResponse(category, q, hasContext) {
        // Standard info, but shorter, adapted for context, and conversational
        const responses = {
            programs: {
                short: `We organize programs by selectivity. {{Accessible programs}} are entry-level STEM opportunities. {{Achievable programs}} come from competitive universities. {{Top-Tier programs}} are elite (MIT, Stanford level). ${safeNavLink(links.programs, 'Browse all programs here')} or ${hasContext ? 'continue exploring what interests you' : 'start with Accessible to get a feel for things'}.`,
                full: `There are three levels of programs. Accessible programs are entry points—easier to get into, still valuable learning. Achievable programs are competitive—you need solid prep but they're reachable. Top-Tier programs are elite—they attract the best students globally. Each teaches you something different, and there's nothing wrong with any level. Most successful people started at a lower level than where they ended up. The important thing is picking the right starting point for you and building from there. ${safeNavLink(links.programs, 'Explore programs by level here')}.`
            },
            writing: {
                short: `Essays work like this: intro (tell them what you'll say), body (show them evidence), conclusion (tell them what it meant). Read examples to see it in action, then practice. That's the recipe.`,
                full: `Good essays follow a consistent structure. You open with context and your main argument (called a thesis). Then you develop that argument with evidence, examples, and explanation—usually in multiple paragraphs. Finally, you close by reflecting on what it all means. The professionals aren't doing anything secret—they're just executing this pattern well through practice. The best way to learn is to study examples that use this structure, then try writing on the same topic, then compare. That read-write-compare cycle is where improvement happens. {{${safeNavLink(links.writingBasics, 'See the structure guide')}}} and {{${safeNavLink(links.writingExamples, 'study real examples')}}} to get started.`
            },
            scholarships: {
                short: `Scholarships come in flavors: merit-based (grades/scores), need-based (financial help), and program-specific (tied to certain programs). Most competitive programs include funding. {{${safeNavLink(links.programs, 'Browse programs with funding')}}} to see what's available.`,
                full: `Scholarships break down into three main categories. Merit-based scholarships reward your achievements—grades, test scores, awards. They say "you've earned this." Need-based scholarships help students whose families need financial support—they consider your situation. Program-based scholarships are built into specific programs or fields. Here's the practical insight: funding is usually part of the program package, not something you hunt separately. When you find a program that interests you, look at what financial options come with it. Most STEM programs have some form of aid to make opportunities accessible.`
            },
            admissions: {
                short: `Admissions to STEM Beheira go through the Ministry of Education. You take the official exam, they score it, they assign placements. It's transparent and fair. {{${safeNavLink(links.admissions, 'Full timeline here')}}}`,
                full: `Here's how admissions work in Egypt. The Ministry of Education runs a national exam for all STEM schools. You complete Grade 9, register for the exam (with a specific timeline), study if you want to improve your score, take the official STEM test, and the Ministry publishes results with school placements. Assignments are based on your test score and school availability. It's a centralized, transparent system—no individual applications, no politics. Everyone goes through the same process. That's actually an advantage because it's fair and predictable. If you understand what the exam tests, you can prepare strategically. {{${safeNavLink(links.admissions, 'See the exact timeline and steps here')}}}.`
            },
            navigation: {
                short: `This site has {{${safeNavLink(links.programs, 'Programs')}}} (by difficulty), {{${safeNavLink(links.writingBasics, 'Writing')}}} (guides and examples), {{${safeNavLink(links.admissions, 'Admissions')}}} (official info), and {{${safeNavLink(links.highlights, 'Highlights')}}} (what students are doing). What sounds interesting?`,
                full: `Here's how the site is organized. The {{${safeNavLink(links.programs, 'Programs')}}} section shows opportunities at different levels (Accessible, Achievable, Top-Tier). {{${safeNavLink(links.writingBasics, 'Writing')}}} has guides on structure, examples you can study, and tools to practice with. {{${safeNavLink(links.admissions, 'Admissions')}}} covers the Ministry exam process and timeline. {{${safeNavLink(links.highlights, 'Highlights')}}} showcases student projects and achievements. Most students explore programs first to see what exists, then use writing resources to strengthen their applications. {{${safeNavLink(links.contact, 'Contact us')}}} if you have specific questions.`
            },
            about_robot: {
                short: `I'm an AI assistant here to help you navigate this site and think through your STEM journey. I give guidance and information—I don't make decisions for you. The people who actually make official decisions (Ministry for admissions, teachers for essay feedback) are the ones with authority.`,
                full: `I'm an AI guide built into this site. I'm here to help you explore programs, understand how writing works, learn about scholarships and admissions, and navigate the site. I give information and reasoning to help you think clearly. But I'm not the authority on anything—the Ministry of Education runs admissions, real teachers give essay feedback, your school provides official information. I'm the thinking partner who helps you understand the landscape and make informed choices. I won't predict your admission chances or make decisions for you—that's your job.`
            },
            default: {
                short: `I can help with programs, scholarships, writing, admissions, navigation, or anything else about this site. What would be most useful right now?`,
                full: `I'm here to help you think through STEM opportunities. Ask me about programs (by difficulty level), scholarships (how to find funding), writing (how to improve), admissions (the process and timeline), or how to navigate this site. I try to give you useful information and help you reason through decisions—but the final choices are yours.`
            }
        };

        const resp = responses[category] || responses.default;
        // Use short by default, full if user seems to want more detail
        const wantsDetail = q.includes('explain') || q.includes('more') || q.includes('detail') || q.includes('how') || q.includes('process');
        return wantsDetail ? resp.full : resp.short;
    }

    function getResponse(raw) {
        const q = (raw || '').toLowerCase().trim();

        // Empty input
        if (!q) {
            const greetings = [
                'I\'m here to help! Ask me about programs, scholarships, writing, admissions, or how to navigate the site.',
                'What can I help you explore today? Programs, writing, scholarships, or admissions?',
                'Ask me anything about STEM opportunities, improving your writing, scholarships, or the application process.'
            ];
            return greetings[Math.floor(Math.random() * greetings.length)];
        }

        // Record conversation
        sessionState.conversationHistory.push({ role: 'user', text: q });

        // Detect intent with multi-layer analysis (including session context)
        const previousTopics = sessionState.exploredTopics || new Set();
        const { category, questionType, hasUncertainty, isVague } = detectIntentAndType(q, previousTopics);
        recordTopic(category);

        // Get topic history for contextual responses
        const topicHistory = getTopicHistory();

        // Build adaptive response based on intent type and context
        let response;
        if (questionType === 'guidance') {
            response = buildGuidanceResponse(category, q, topicHistory.length > 0);
        } else if (questionType === 'decision') {
            response = buildDecisionResponse(category, q, topicHistory.length > 0);
        } else if (questionType === 'clarification') {
            // If user seems genuinely confused, provide extra clarity
            if (isVague && hasUncertainty) {
                response = buildClarificationResponse(category, q);
                // Add encouragement for vague questions
                response = response + ' ' + (sessionState.clarifyingAttempts < 2 ?
                    'If you can give me a bit more detail, I can help even better.' :
                    'Feel free to ask in a different way if that didn\'t help.');
            } else {
                response = buildClarificationResponse(category, q);
            }
        } else if (questionType === 'followup') {
            response = buildFollowupResponse(category, q, topicHistory);
        } else {
            // Standard information, with context awareness
            response = buildInformationResponse(category, q, topicHistory.length > 0);
        }

        // For very vague questions, offer to clarify
        if (isVague && !q.includes('?') && topicHistory.length > 0) {
            response = response + ` ${topicHistory.length > 2 ? '(Or let me know if you meant something different.)' : '(Ask me anything specific and I\'ll dive deeper.)'}`;
        }

        // Record response
        sessionState.conversationHistory.push({ role: 'bot', text: response });

        // Track clarifying attempts
        if (questionType === 'clarification') {
            sessionState.clarifyingAttempts = (sessionState.clarifyingAttempts || 0) + 1;
        } else {
            sessionState.clarifyingAttempts = 0;
        }

        return response;
    }

    function openPanel() {
        panel.classList.add('is-open');
        toggle.setAttribute('aria-expanded', 'true');
        input.focus();
    }

    function closePanel() {
        panel.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
    }

    function sendMessage() {
        const text = input.value.trim();
        if (!text) return;
        addMessage('user', text);
        const reply = getResponse(text);
        addMessage('bot', reply);
        input.value = '';
    }

    toggle.addEventListener('click', () => {
        if (panel.classList.contains('is-open')) closePanel();
        else openPanel();
        toggle.classList.add('assistant-pulse');
        setTimeout(() => toggle.classList.remove('assistant-pulse'), 200);
    });

    closeBtn?.addEventListener('click', closePanel);

    sendBtn.addEventListener('click', sendMessage);
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            sendMessage();
        }
    });

    if (quickWrap) {
        quickWrap.addEventListener('click', (e) => {
            const btn = e.target.closest('button[data-question]');
            if (!btn) return;
            input.value = btn.dataset.question;
            sendMessage();
        });
    }

    if (!reducedMotion && eyes.length) {
        document.addEventListener('mousemove', (e) => {
            const { innerWidth, innerHeight } = window;
            const x = (e.clientX / innerWidth - 0.5) * 8;
            const y = (e.clientY / innerHeight - 0.5) * 8;
            eyes.forEach((eye) => {
                eye.style.transform = `translate(${x}px, ${y}px)`;
            });
        });
    }
})();