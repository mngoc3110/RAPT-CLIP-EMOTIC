class_names_5 = [
    "Neutral (student in class).",
    "Enjoyment (student in class).",
    "Confusion (student in class).",
    "Fatigue (student in class).",
    "Distraction (student in class)."
]

class_names_with_context_5 = [
    "A student shows a neutral learning state in a classroom.",
    "A student shows enjoyment while learning in a classroom.",
    "A student shows confusion during learning in a classroom.",
    "A student shows fatigue during learning in a classroom.",
    "A student shows distraction and is not focused in a classroom."
]

class_descriptor_5_only_face = [
    "A student has a neutral face with relaxed mouth, open eyes, and calm eyebrows.",
    "A student looks happy with a slight smile, bright eyes, and relaxed eyebrows.",
    "A student looks confused with furrowed eyebrows, a puzzled look, and slightly open mouth.",
    "A student looks tired with drooping eyelids, frequent yawning, and a sleepy face.",
    "A student looks distracted with unfocused eyes and a wandering gaze away from the lesson."
]

class_descriptor_5_only_body = [
    "A student sits still with an upright posture and hands on the desk, showing a neutral learning state.",
    "A student leans slightly forward with an open, engaged posture, showing enjoyment in learning.",
    "A student tilts the head and leans in, hand on chin, showing confusion while trying to understand.",
    "A student slouches with shoulders dropped and head lowered, showing fatigue during class.",
    "A student shifts around, turns away from the desk, or looks sideways, showing distraction and low focus."
]

class_descriptor_5 = [
    "A student looks neutral and calm in class, with a relaxed face and steady gaze, quietly watching the lecture or reading notes.",
    "A student shows enjoyment while learning, with a gentle smile and bright eyes, appearing engaged and interested in the lesson.",
    "A student looks confused in class, with furrowed eyebrows and a puzzled expression, focusing on the material as if trying to understand.",
    "A student appears fatigued in class, with drooping eyelids and yawning, head slightly lowered, showing low energy.",
    "A student is distracted in class, frequently looking away from the lesson, scanning around, and not paying attention to learning materials."
]

# Prompt Ensemble for RAER (5 classes)
# Each inner list contains multiple descriptions for a single class.
prompt_ensemble_5 = [
    [   # Neutral
        "A photo of a student being alert and looking straight ahead.",
        "A photo of a student with a calm and steady gaze.",
        "A photo of a student paying attention with a neutral expression."
    ],
    [   # Enjoyment
        "A photo of a student smiling and looking happy.",
        "A photo of a student showing joy and enthusiasm.",
        "A photo of a student appearing pleased and engaged."
    ],
    [   # Confusion
        "A photo of a student frowning with a puzzled expression.",
        "A photo of a student scratching their head or looking confused.",
        "A photo of a student trying hard to understand but failing."
    ],
    [   # Fatigue
        "A photo of a student yawning or falling asleep.",
        "A photo of a student with heavy drooping eyelids.",
        "A photo of a student resting their head, looking very tired."
    ],
    [   # Distraction
        "A photo of a student looking away from the screen.",
        "A photo of a student turning their head to the side.",
        "A photo of a student engaging in other activities, not studying."
    ]
]

class_descriptor_8 = [
    'A person who is feeling neutral.',
    'A person who is feeling happy.',
    'A person who is feeling sad.',
    'A person who is feeling surprise.',
    'A person who is feeling fear.',
    'A person who is feeling disgust.',
    'A person who is feeling anger.',
    'A person who is feeling contempt.'
]

class_names_8 = [
    'Neutral', 'Happy', 'Sad', 'Surprise', 'Fear', 'Disgust', 'Anger', 'Contempt'
]

class_names_7 = ['Neutral', 'Happy', 'Sad', 'Surprise', 'Fear', 'Disgust', 'Anger']

class_descriptor_7 = [
    'A person who is feeling neutral.',
    'A person who is feeling happy.',
    'A person who is feeling sad.',
    'A person who is feeling surprise.',
    'A person who is feeling fear.',
    'A person who is feeling disgust.',
    'A person who is feeling anger.'
]

class_names_with_context_7 = [
    'A person shows neutral emotion.',
    'A person shows happy emotion.',
    'A person shows sad emotion.',
    'A person shows surprise emotion.',
    'A person shows fear emotion.',
    'A person shows disgust emotion.',
    'A person shows anger emotion.'
]

class_descriptor_7_only_face = [
    'The face of a person who is feeling neutral.',
    'The face of a person who is feeling happy.',
    'The face of a person who is feeling sad.',
    'The face of a person who is feeling surprise.',
    'The face of a person who is feeling fear.',
    'The face of a person who is feeling disgust.',
    'The face of a person who is feeling anger.'
]

class_descriptor_7_only_body = [
    'The body of a person who is feeling neutral.',
    'The body of a person who is feeling happy.',
    'The body of a person who is feeling sad.',
    'The body of a person who is feeling surprise.',
    'The body of a person who is feeling fear.',
    'The body of a person who is feeling disgust.',
    'The body of a person who is feeling anger.'
]

class_names_with_context_8 = [
    'A person shows neutral emotion.',
    'A person shows happy emotion.',
    'A person shows sad emotion.',
    'A person shows surprise emotion.',
    'A person shows fear emotion.',
    'A person shows disgust emotion.',
    'A person shows anger emotion.',
    'A person shows contempt emotion.'
]

class_descriptor_8_only_face = [
    'The face of a person who is feeling neutral.',
    'The face of a person who is feeling happy.',
    'The face of a person who is feeling sad.',
    'The face of a person who is feeling surprise.',
    'The face of a person who is feeling fear.',
    'The face of a person who is feeling disgust.',
    'The face of a person who is feeling anger.',
    'The face of a person who is feeling contempt.'
]

class_descriptor_8_only_body = [
    'The body of a person who is feeling neutral.',
    'The body of a person who is feeling happy.',
    'The body of a person who is feeling sad.',
    'The body of a person who is feeling surprise.',
    'The body of a person who is feeling fear.',
    'The body of a person who is feeling disgust.',
    'The body of a person who is feeling anger.',
    'The body of a person who is feeling contempt.'
]

# CK+ Classes (Alphabetical Order: Anger, Contempt, Disgust, Fear, Happy, Sadness, Surprise)
class_names_ckplus = ['Anger', 'Contempt', 'Disgust', 'Fear', 'Happy', 'Sadness', 'Surprise']

class_names_with_context_ckplus = [
    "A person shows anger.",
    "A person shows contempt.",
    "A person shows disgust.",
    "A person shows fear.",
    "A person shows happiness.",
    "A person shows sadness.",
    "A person shows surprise."
]

class_descriptor_ckplus = [
    "A person with an angry expression, furrowed brows and tightened lips.",
    "A person with a contemptuous expression, one corner of the lip raised.",
    "A person with a disgusted expression, nose wrinkled and upper lip raised.",
    "A person with a fearful expression, eyes wide open and eyebrows raised.",
    "A person with a happy expression, smiling with cheeks raised.",
    "A person with a sad expression, corners of the lips turned down and drooping eyelids.",
    "A person with a surprised expression, mouth open and eyes widened."
]

prompt_ensemble_ckplus = [
    [ # Anger
        "A photo of a person showing anger.",
        "A face with furrowed brows and a glare.",
        "An angry facial expression."
    ],
    [ # Contempt
        "A photo of a person showing contempt.",
        "A face with a smirk or sneer.",
        "A contemptuous facial expression."
    ],
    [ # Disgust
        "A photo of a person showing disgust.",
        "A face with a wrinkled nose.",
        "A disgusted facial expression."
    ],
    [ # Fear
        "A photo of a person showing fear.",
        "A face with wide eyes and a terrified look.",
        "A fearful facial expression."
    ],
    [ # Happy
        "A photo of a person showing happiness.",
        "A smiling face with joy.",
        "A happy facial expression."
    ],
    [ # Sadness
        "A photo of a person showing sadness.",
        "A face with a frown and sorrowful eyes.",
        "A sad facial expression."
    ],
    [ # Surprise
        "A photo of a person showing surprise.",
        "A face with an open mouth and wide eyes.",
        "A surprised facial expression."
    ]
]

# SFER Classes (Alphabetical: Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise)
class_names_sfer = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

class_names_with_context_sfer = [
    "A student shows anger.",
    "A student shows disgust.",
    "A student shows fear.",
    "A student shows happiness.",
    "A student shows neutrality.",
    "A student shows sadness.",
    "A student shows surprise."
]

class_descriptor_sfer = [
    "A student with an angry expression, furrowed brows and tightened lips.",
    "A student with a disgusted expression, nose wrinkled and upper lip raised.",
    "A student with a fearful expression, eyes wide open and eyebrows raised.",
    "A student with a happy expression, smiling with cheeks raised.",
    "A student with a neutral expression, relaxed face and calm gaze.",
    "A student with a sad expression, corners of the lips turned down and drooping eyelids.",
    "A student with a surprised expression, mouth open and eyes widened."
]

prompt_ensemble_sfer = [
    [ # Anger
        "A photo of a student showing anger.",
        "A face with furrowed brows and a glare.",
        "An angry facial expression."
    ],
    [ # Disgust
        "A photo of a student showing disgust.",
        "A face with a wrinkled nose.",
        "A disgusted facial expression."
    ],
    [ # Fear
        "A photo of a student showing fear.",
        "A face with wide eyes and a terrified look.",
        "A fearful facial expression."
    ],
    [ # Happy
        "A photo of a student showing happiness.",
        "A smiling face with joy.",
        "A happy facial expression."
    ],
    [ # Neutral
        "A photo of a student showing a neutral expression.",
        "A calm face with no strong emotion.",
        "A neutral facial expression."
    ],
    [ # Sad
        "A photo of a student showing sadness.",
        "A face with a frown and sorrowful eyes.",
        "A sad facial expression."
    ],
    [ # Surprise
        "A photo of a student showing surprise.",
        "A face with an open mouth and wide eyes.",
        "A surprised facial expression."
    ]
]

# CAER Classes (Alphabetical: Anger, Disgust, Fear, Happy, Neutral, Sad, Surprise)
class_names_caer = ['Anger', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

class_names_with_context_caer = [
    "A person shows anger.",
    "A person shows disgust.",
    "A person shows fear.",
    "A person shows happiness.",
    "A person shows neutrality.",
    "A person shows sadness.",
    "A person shows surprise."
]

class_descriptor_caer = [
    "A person with an angry expression, furrowed brows and tightened lips.",
    "A person with a disgusted expression, nose wrinkled and upper lip raised.",
    "A person with a fearful expression, eyes wide open and eyebrows raised.",
    "A person with a happy expression, smiling with cheeks raised.",
    "A person with a neutral expression, relaxed face and calm gaze.",
    "A person with a sad expression, corners of the lips turned down and drooping eyelids.",
    "A person with a surprised expression, mouth open and eyes widened."
]

prompt_ensemble_caer = [
    [ # Anger
        "A scene from a movie showing a person in an angry confrontation.",
        "A person with an angry face in a tense and hostile environment.",
        "A photo of an actor expressing rage during a dramatic cinematic scene."
    ],
    [ # Disgust
        "A person showing a disgusted expression in a repulsive or unpleasant situation.",
        "A movie scene where someone reacts with revulsion to something gross.",
        "A cinematic shot of a face showing strong dislike and disgust."
    ],
    [ # Fear
        "A person showing fear in a dark, mysterious, or threatening environment.",
        "A scene from a suspenseful movie where an actor looks absolutely terrified.",
        "A cinematic photo of a fearful face during a scary and tense moment."
    ],
    [ # Happy
        "A person feeling happy and celebrating in a bright, social movie scene.",
        "A joyful actor in a pleasant environment showing a wide smile.",
        "A scene showing a happy facial expression during a positive and cheerful event."
    ],
    [ # Neutral
        "A person with a neutral expression in a mundane, everyday cinematic scene.",
        "A calm and expressionless actor in a casual movie background.",
        "A photo of someone showing no specific emotion in a normal setting."
    ],
    [ # Sad
        "A person showing sadness and grief in a gloomy or lonely cinematic environment.",
        "A scene from a dramatic movie where an actor looks heartbroken and sorrowful.",
        "A cinematic photo of a sad face in a somber, quiet, and melancholic setting."
    ],
    [ # Surprise
        "A person showing great surprise at an unexpected event in a dynamic scene.",
        "A shocked facial expression during a surprising and dramatic movie moment.",
        "A cinematic shot of an actor looking amazed or startled by something sudden."
    ]
]

class_descriptor_caer_only_face = [
    'The face of a person who is feeling anger, with furrowed brows, tightened lips, and a glaring look.',
    'The face of a person who is feeling disgust, with a wrinkled nose and a raised upper lip.',
    'The face of a person who is feeling fear, with wide open eyes and raised, tensed eyebrows.',
    'The face of a person who is feeling happy, with a wide smile, raised cheeks, and bright eyes.',
    'The face of a person who is feeling neutral, with a relaxed expression and a calm, steady gaze.',
    'The face of a person who is feeling sad, with corners of the lips turned down and drooping eyelids.',
    'The face of a person who is feeling surprise, with an open mouth and very wide, startled eyes.'
]

class_names_daisee = ['Very Low', 'Low', 'High', 'Very High']

class_names_with_context_daisee = [
    "A student shows very low engagement.",
    "A student shows low engagement.",
    "A student shows high engagement.",
    "A student shows very high engagement."
]

class_descriptor_daisee = [
    "A student is completely disengaged, looking away, sleeping, or doing something else entirely.",
    "A student is distracted, frequently looking around, yawning, or showing little interest.",
    "A student is paying attention, looking at the screen, and following the lesson.",
    "A student is highly focused, leaning forward, taking notes, and reacting to the content."
]

prompt_ensemble_daisee = [
    [ # Very Low (0)
        "A video of a student with very low engagement.",
        "A student looking away or sleeping.",
        "A completely disengaged student."
    ],
    [ # Low (1)
        "A video of a student with low engagement.",
        "A student looking distracted or bored.",
        "A student showing little interest in the lesson."
    ],
    [ # High (2)
        "A video of a student with high engagement.",
        "A student looking at the screen attentively.",
        "A student following the lecture."
    ],
    [ # Very High (3)
        "A video of a highly engaged student.",
        "A student leaning forward and taking notes.",
        "A student completely absorbed in learning."
    ]
]

# EMOTIC Classes (Standard 26 categories)
class_names_emotic = [
    'Affection', 'Anger', 'Annoyance', 'Anticipation', 'Aversion', 'Confidence', 'Disapproval', 
    'Disconnection', 'Disquietment', 'Doubt/Confusion', 'Embarrassment', 'Engagement', 'Esteem', 
    'Excitement', 'Fatigue', 'Fear', 'Happiness', 'Pain', 'Peace', 'Pleasure', 'Sadness', 
    'Sensitivity', 'Suffering', 'Surprise', 'Sympathy', 'Yearning'
]

class_names_with_context_emotic = [f"A person shows {name.lower()} in their environment." for name in class_names_emotic]

class_descriptor_emotic = [
    # 0 - Affection
    "A person showing warmth and love, hugging, holding hands, leaning close, or tenderly touching someone with a gentle smile and soft eyes.",
    # 1 - Anger
    "A person expressing rage or fury with clenched fists, tense body, furrowed brows, gritted teeth, and an aggressive or confrontational posture.",
    # 2 - Annoyance
    "A person looking mildly irritated with a slight frown, rolled eyes, crossed arms, or a dismissive gesture, bothered by something in their surroundings.",
    # 3 - Anticipation
    "A person eagerly waiting or expecting something, leaning forward with wide attentive eyes, raised eyebrows, and an alert, ready posture.",
    # 4 - Aversion
    "A person turning away, recoiling, or shielding themselves from something unpleasant, with a wrinkled nose, averted gaze, and defensive body language.",
    # 5 - Confidence
    "A person standing tall with an upright posture, chin raised, chest out, steady direct gaze, and a composed or self-assured expression.",
    # 6 - Disapproval
    "A person expressing moral judgment or criticism with a stern face, pursed lips, head shake, furrowed brows, or a disapproving pointed gesture.",
    # 7 - Disconnection
    "A person appearing emotionally detached or isolated, sitting alone, gazing blankly, arms folded inward, turned away from others in the scene.",
    # 8 - Disquietment
    "A person showing anxiety or unease with restless fidgeting, tense shoulders, a worried furrowed brow, and nervous glancing around.",
    # 9 - Doubt/Confusion
    "A person looking puzzled or uncertain, tilting their head, scratching their chin, squinting, with furrowed eyebrows and a perplexed expression.",
    # 10 - Embarrassment
    "A person feeling self-conscious, covering their face, looking down, blushing, with hunched shoulders and an awkward, shy posture in front of others.",
    # 11 - Engagement
    "A person fully absorbed and focused on an activity, leaning in with intent eyes, active hand gestures, and a concentrated or interested expression.",
    # 12 - Esteem
    "A person showing admiration or respect toward someone, with an approving nod, warm proud smile, clapping, or a gesture of recognition and honor.",
    # 13 - Excitement
    "A person expressing thrill and enthusiasm with jumping, clapping, wide sparkling eyes, a big open smile, raised arms, and energetic body movement.",
    # 14 - Fatigue
    "A person looking exhausted with drooping eyelids, yawning, slouched shoulders, a heavy head resting on their hand, and slow lethargic movement.",
    # 15 - Fear
    "A person showing terror or fright with wide panicked eyes, a frozen or cowering posture, mouth agape, hands raised defensively, and a tense rigid body.",
    # 16 - Happiness
    "A person feeling joyful with a bright genuine smile, relaxed open posture, sparkling eyes, and an overall warm pleasant demeanor in their environment.",
    # 17 - Pain
    "A person in physical or emotional distress, grimacing, clutching a body part, with a contorted face, wincing eyes, and a strained uncomfortable posture.",
    # 18 - Peace
    "A person in a tranquil calm state, with relaxed muscles, a serene gentle expression, closed or soft eyes, and a still composed body in a quiet setting.",
    # 19 - Pleasure
    "A person savoring enjoyment or satisfaction, with a content smile, relaxed closed eyes, a leaned-back comfortable posture, and a look of gratification.",
    # 20 - Sadness
    "A person expressing grief or sorrow with downcast eyes, drooping mouth corners, slumped shoulders, a bowed head, and a withdrawn melancholic posture.",
    # 21 - Sensitivity
    "A person being emotionally reactive, with teary glistening eyes, a quivering lip, hand on chest, and a delicate vulnerable expression showing deep feeling.",
    # 22 - Suffering
    "A person enduring hardship or anguish with a pained expression, clenched jaw, bowed body, gripping hands, and visible emotional or physical torment.",
    # 23 - Surprise
    "A person reacting to something unexpected with raised eyebrows, wide open eyes, an open mouth, a sudden jerk backward, and a startled astonished look.",
    # 24 - Sympathy
    "A person showing compassionate concern for another, with a gentle tilted head, soft eyes, a comforting touch or embrace, and a caring worried expression.",
    # 25 - Yearning
    "A person displaying longing or deep desire, gazing wistfully into the distance, reaching out, with a bittersweet expression and a tense hopeful posture.",
]

prompt_ensemble_emotic = [
    [   # 0 - Affection
        "A person hugging or holding someone with warmth and love.",
        "An intimate moment of tenderness between people in a real setting.",
        "A caring person gently touching or embracing another, showing deep fondness.",
        "A scene of affectionate closeness, with gentle smiles and soft body language.",
        "A person leaning toward someone they love with open arms and a warm expression.",
        "Two people sharing an affectionate bond through touch and loving eye contact.",
        "A warm scene showing a person expressing love and care toward another.",
    ],
    [   # 1 - Anger
        "A person with a furious expression, clenched fists, and an aggressive stance.",
        "An angry confrontation where a person shows hostility with tense muscles and a glare.",
        "A person expressing rage with furrowed brows, bared teeth, and a threatening posture.",
        "A heated argument scene with a person pointing aggressively and shouting.",
        "A furious person displaying intense displeasure through body tension and facial anger.",
        "A person in a hostile environment expressing fury with tight jaw and fierce eyes.",
        "An enraged individual with a confrontational posture and visible anger in their face.",
    ],
    [   # 2 - Annoyance
        "A person rolling their eyes or sighing with mild irritation.",
        "An annoyed person with crossed arms and a dismissive expression.",
        "A person visibly bothered by something, frowning slightly and looking away.",
        "Someone showing mild frustration with a tight-lipped expression and impatient gestures.",
        "A mildly irritated person tapping their foot or drumming fingers impatiently.",
        "A scene where a person looks displeased and bothered by their surroundings.",
        "An individual with a subtle frown and narrowed eyes showing annoyance.",
    ],
    [   # 3 - Anticipation
        "A person eagerly leaning forward, waiting for something with bright attentive eyes.",
        "An expectant individual on the edge of their seat with raised eyebrows and alert posture.",
        "A person looking ahead with excitement and readiness for what is about to happen.",
        "Someone waiting with bated breath, eyes wide and body tense with expectation.",
        "A person showing eager anticipation with an alert focused gaze and forward lean.",
        "An individual watching intently, ready and prepared for an upcoming event.",
        "A person with a hopeful expression looking forward to something with visible excitement.",
    ],
    [   # 4 - Aversion
        "A person recoiling or turning away from something disgusting or repulsive.",
        "Someone covering their nose and looking away with strong dislike and revulsion.",
        "A person with a wrinkled nose and averted gaze, avoiding something unpleasant.",
        "An individual physically pulling back from something that causes deep discomfort.",
        "A person shielding themselves and grimacing at something they find revolting.",
        "Someone showing strong repulsion with a turned body and a look of disgust.",
        "A person displaying aversion by stepping back with arms raised defensively.",
    ],
    [   # 5 - Confidence
        "A person standing tall with their chest out, chin up, and a self-assured expression.",
        "A confident individual walking with purpose, making direct eye contact and smiling.",
        "A person in a powerful pose, exuding certainty and self-belief in their stance.",
        "Someone speaking assertively with open gestures and a composed, steady gaze.",
        "A person displaying confidence with relaxed shoulders, upright posture, and calm eyes.",
        "An individual radiating self-assurance through their poised body language and expression.",
        "A self-confident person in their environment with a commanding, comfortable presence.",
    ],
    [   # 6 - Disapproval
        "A person shaking their head with pursed lips and a stern, judgmental expression.",
        "Someone giving a disapproving look with furrowed brows and crossed arms.",
        "A person expressing criticism through a cold stare and a tight-lipped frown.",
        "An individual pointing a finger in a scolding manner with a serious face.",
        "A person conveying moral judgment with a disappointed head tilt and hard eyes.",
        "Someone showing their displeasure at another person's actions with visible disapproval.",
        "A person with an expression of moral condemnation, looking stern and unyielding.",
    ],
    [   # 7 - Disconnection
        "A person sitting alone, staring blankly with an emotionally detached expression.",
        "An isolated individual turned away from a group, lost in their own thoughts.",
        "A person gazing absently into space, physically present but mentally elsewhere.",
        "Someone appearing withdrawn and separated from the people around them.",
        "A person with a vacant expression, arms folded, showing emotional isolation.",
        "An individual who appears checked out, disconnected from the activity around them.",
        "A lonely person in a crowd, showing detachment through distant eyes and closed posture.",
    ],
    [   # 8 - Disquietment
        "A person fidgeting nervously with tense shoulders and a worried furrowed brow.",
        "An anxious individual glancing around restlessly with visible unease.",
        "A person biting their nails or wringing hands, showing inner turmoil and restlessness.",
        "Someone pacing or shifting weight from foot to foot with a troubled expression.",
        "A person showing discomfort and anxiety through hunched posture and darting eyes.",
        "An uneasy individual with a strained expression and nervous body movements.",
        "A person in an unsettling environment showing visible signs of worry and agitation.",
    ],
    [   # 9 - Doubt/Confusion
        "A person scratching their head with a puzzled, uncertain expression.",
        "Someone squinting and tilting their head, trying to understand something confusing.",
        "A bewildered person with furrowed eyebrows and an open mouth of confusion.",
        "An individual looking back and forth with doubt, unsure of what to do next.",
        "A person with a quizzical expression, hand on chin, deep in uncertain thought.",
        "Someone with raised eyebrows and a lost look, clearly confused by the situation.",
        "A perplexed person showing uncertainty through hesitant gestures and a puzzled face.",
    ],
    [   # 10 - Embarrassment
        "A person covering their face with their hands, blushing with embarrassment.",
        "Someone looking down shyly with hunched shoulders in an awkward social moment.",
        "A person turning red and avoiding eye contact after a humiliating situation.",
        "An individual hiding behind their hands or hair, visibly self-conscious and ashamed.",
        "A person fidgeting nervously while others watch, showing clear embarrassment.",
        "Someone cringing and shrinking away with a mortified expression on their face.",
        "A self-conscious person trying to make themselves small in an uncomfortable situation.",
    ],
    [   # 11 - Engagement
        "A person fully focused on a task, leaning in with concentrated, intent eyes.",
        "An engaged individual actively participating with animated hand gestures and interest.",
        "A person deeply absorbed in conversation or an activity with focused attention.",
        "Someone listening intently with their body leaned forward and eyes locked on the subject.",
        "A person showing deep involvement through an alert posture and responsive expressions.",
        "An individual completely immersed in what they are doing with visible concentration.",
        "A person actively working or interacting, fully occupied and interested in the task.",
    ],
    [   # 12 - Esteem
        "A person clapping or nodding approvingly at someone with a proud, warm smile.",
        "Someone looking at another with admiration, respect, and recognition in their eyes.",
        "A person giving a standing ovation or a respectful gesture of honor and praise.",
        "An individual showing deep respect with a warm approving gaze and upright posture.",
        "A person congratulating or acknowledging someone's achievement with genuine pride.",
        "Someone expressing high regard for another through their attentive, respectful demeanor.",
        "A person showing admiration by watching someone with warmth and an approving expression.",
    ],
    [   # 13 - Excitement
        "A person jumping with joy, arms raised high, and eyes sparkling with thrill.",
        "An excited individual clapping and cheering with a wide, energetic open-mouth smile.",
        "A person pumping their fist in celebration, full of enthusiasm and energy.",
        "Someone bouncing on their feet with an ecstatic expression and animated gestures.",
        "A thrilled person showing exhilaration with rapid movements and a beaming face.",
        "An individual celebrating with visible delight, arms spread wide with pure excitement.",
        "A person at a lively event showing intense excitement through their whole body.",
    ],
    [   # 14 - Fatigue
        "A person yawning widely with drooping heavy eyelids and a slumped posture.",
        "An exhausted individual resting their head on their hand with half-closed eyes.",
        "A person struggling to stay awake, slouching with slow, lethargic movements.",
        "Someone rubbing their tired eyes with drooping shoulders and a weary expression.",
        "A fatigued person barely able to keep their eyes open, sitting with low energy.",
        "An individual showing complete exhaustion through a limp posture and blank tired face.",
        "A person in a drowsy state, head nodding forward, fighting to stay conscious.",
    ],
    [   # 15 - Fear
        "A person with wide terrified eyes, frozen body, and mouth open in horror.",
        "A frightened individual cowering with hands raised defensively and a panicked look.",
        "A person backing away from a threat with a rigid body and a tense, scared face.",
        "Someone screaming or gasping in fear with dilated pupils and trembling hands.",
        "A terrified person clutching something for safety with visible dread in their posture.",
        "An individual showing pure fear with a pale face, clenched body, and wide eyes.",
        "A person in a dark or threatening setting, expressing terror through frozen body language.",
    ],
    [   # 16 - Happiness
        "A person with a bright, genuine smile, relaxed shoulders, and warm sparkling eyes.",
        "A happy individual laughing heartily with an open, joyful expression in a pleasant scene.",
        "A person radiating contentment with a gentle smile, comfortable posture, and calm energy.",
        "Someone smiling broadly with crinkled eyes, showing pure joy and a carefree mood.",
        "A delighted person with a relaxed, open body language and a beaming cheerful face.",
        "An individual in a happy moment, sharing laughter or a warm smile with others.",
        "A joyful person in a bright environment expressing pleasure through their whole being.",
    ],
    [   # 17 - Pain
        "A person grimacing and clutching a body part, showing visible physical distress.",
        "Someone wincing with a contorted face and strained posture, clearly in pain.",
        "A person doubled over, holding their stomach or head, expressing sharp discomfort.",
        "An individual gritting their teeth with tightly squeezed eyes and a pained expression.",
        "A person reacting to an injury with a sudden jerk, tensed muscles, and a cry of pain.",
        "Someone showing suffering through a twisted grimace and a protective body curl.",
        "A person in visible agony, with tears forming and hands pressing on the painful area.",
    ],
    [   # 18 - Peace
        "A person sitting calmly with closed eyes, a serene expression, and relaxed shoulders.",
        "A tranquil individual resting peacefully in a quiet, soothing natural environment.",
        "A person meditating or sitting still with a gentle, content smile and soft breathing.",
        "Someone gazing peacefully at a calm landscape with a relaxed, open posture.",
        "A person in a state of inner calm, with smooth features and loose, comfortable limbs.",
        "An individual lying back or sitting quietly with a blissful, undisturbed expression.",
        "A person enjoying a moment of stillness, radiating serenity and quiet satisfaction.",
    ],
    [   # 19 - Pleasure
        "A person savoring a delightful experience with closed eyes and a content smile.",
        "Someone leaning back in satisfaction, enjoying a moment of personal gratification.",
        "A person eating, drinking, or experiencing something pleasurable with visible delight.",
        "An individual showing enjoyment through a relaxed body and a gratified expression.",
        "A person relishing a moment with a slow smile and a look of deep satisfaction.",
        "Someone indulging in a pleasurable activity with a relaxed, happy demeanor.",
        "A person experiencing sensory enjoyment, looking content and fulfilled in the moment.",
    ],
    [   # 20 - Sadness
        "A person with tears rolling down, a bowed head, and slumped shoulders showing grief.",
        "A sad individual sitting alone with a downcast gaze and a heavy, sorrowful expression.",
        "A person crying or wiping tears with drooping mouth corners and a pained face.",
        "Someone standing in the rain or a gloomy setting, looking heartbroken and lonely.",
        "A melancholic person with hollow eyes, a pale face, and a withdrawn defeated posture.",
        "An individual expressing deep sorrow through quiet sobbing and a fragile body language.",
        "A grieving person with their hand over their heart, showing emotional pain and loss.",
    ],
    [   # 21 - Sensitivity
        "A person with glistening teary eyes and a quivering lip, deeply moved by something.",
        "Someone placing a hand on their chest, emotionally touched and visibly affected.",
        "A person reacting to a tender moment with watery eyes and a gentle, moved expression.",
        "An individual showing vulnerability, their face softening in response to an emotional scene.",
        "A person tearing up at a kind gesture, showing heightened emotional responsiveness.",
        "Someone visibly affected by a small emotional trigger, looking fragile and open.",
        "A person showing deep emotional sensitivity through a trembling expression and moist eyes.",
    ],
    [   # 22 - Suffering
        "A person in visible anguish, hunched over with a contorted face and clenched fists.",
        "Someone enduring deep emotional or physical torment with a hollow, exhausted look.",
        "A person gripping their head or body in sustained pain and distress.",
        "An individual showing prolonged hardship through a defeated, broken posture and pained eyes.",
        "A person bearing heavy burden shown through strained muscles and a tormented expression.",
        "Someone collapsed or slumped in despair, showing the weight of prolonged suffering.",
        "A person in a harsh environment showing resilience mixed with visible agony and strain.",
    ],
    [   # 23 - Surprise
        "A person with raised eyebrows, wide open eyes, and an open mouth of astonishment.",
        "Someone jerking backward with a startled expression at something unexpected.",
        "A person gasping with hands flying to their mouth in complete shock and amazement.",
        "An individual with dilated eyes and a frozen posture, caught completely off guard.",
        "A person reacting with a double-take, jaw dropped, at a sudden surprising event.",
        "Someone spinning around with a stunned look to face an unexpected situation.",
        "A person expressing pure astonishment through exaggerated wide eyes and raised hands.",
    ],
    [   # 24 - Sympathy
        "A person comforting someone with a gentle hand on their shoulder and concerned eyes.",
        "Someone listening to another's problems with a tilted head and a caring, soft expression.",
        "A person embracing someone in distress, showing deep compassion and understanding.",
        "An individual offering a tissue or comfort with a worried, empathetic face.",
        "A person sitting beside someone in pain, showing solidarity through their gentle presence.",
        "Someone with a sad, caring expression reaching out to console a person who is upset.",
        "A compassionate person showing concern and support through their warm, attentive body language.",
    ],
    [   # 25 - Yearning
        "A person gazing wistfully into the distance with a bittersweet, longing expression.",
        "Someone reaching out toward something they cannot have, with an aching look in their eyes.",
        "A person staring at a photo or an empty space, showing deep desire and nostalgia.",
        "An individual with a faraway look, chin resting on hand, lost in longing thoughts.",
        "A person pressing their hand against a window or barrier, yearning for what lies beyond.",
        "Someone looking at a departing person or place with visible sadness and desperate hope.",
        "A person with a tense, hopeful posture and melancholic eyes, craving something deeply.",
    ],
]

# =============================================================================
# EMOTIC Paper-Based Prompts (Kosti et al., TPAMI 2019, Table 1)
# =============================================================================
# These prompts are derived directly from the official emotion definitions
# in the EMOTIC paper. Optimized for body+context (2-stream, no face).
# Reference: "Context Based Emotion Recognition using EMOTIC Dataset"
#            arXiv:2003.13401 / IEEE TPAMI 2019

class_descriptor_emotic_paper = [
    # 0 - Affection: fond feelings; love; tenderness
    "A person displaying fond feelings, love, and tenderness toward another person in their surroundings.",
    # 1 - Anger: intense displeasure or rage; furious; resentful
    "A person showing intense displeasure or rage, appearing furious and resentful in the scene.",
    # 2 - Annoyance: bothered by something or someone; irritated; impatient; frustrated
    "A person who is bothered, irritated, impatient, or frustrated by something or someone around them.",
    # 3 - Anticipation: state of looking forward; hoping on or getting prepared for possible future events
    "A person in a state of looking forward, hoping or getting prepared for possible future events.",
    # 4 - Aversion: feeling disgust, dislike, repulsion; feeling hate
    "A person feeling disgust, dislike, or repulsion toward something in their environment.",
    # 5 - Confidence: feeling of being certain; conviction that an outcome will be favorable; encouraged; proud
    "A person feeling certain and proud, with conviction that an outcome will be favorable.",
    # 6 - Disapproval: feeling that something is wrong or reprehensible; contempt; hostile
    "A person feeling that something is wrong or reprehensible, showing contempt or hostility.",
    # 7 - Disconnection: feeling not interested in the main event; indifferent; bored; distracted
    "A person not interested in the main event of their surroundings, appearing indifferent, bored, or distracted.",
    # 8 - Disquietment: nervous; worried; upset; anxious; tense; pressured; alarmed
    "A person who is nervous, worried, upset, anxious, tense, or alarmed in their situation.",
    # 9 - Doubt/Confusion: difficulty to understand or decide; thinking about different options
    "A person having difficulty understanding or deciding, thinking about different options.",
    # 10 - Embarrassment: feeling ashamed or guilty
    "A person feeling ashamed or guilty in the presence of others.",
    # 11 - Engagement: paying attention to something; absorbed into something; curious; interested
    "A person paying close attention, absorbed into an activity, curious and interested.",
    # 12 - Esteem: feelings of favourable opinion or judgement; respect; admiration; gratefulness
    "A person showing respect, admiration, or gratefulness toward someone or something.",
    # 13 - Excitement: feeling enthusiasm; stimulated; energetic
    "A person feeling enthusiasm, stimulated and energetic in an active scene.",
    # 14 - Fatigue: weariness; tiredness; sleepy
    "A person showing weariness, tiredness, or sleepiness in their current setting.",
    # 15 - Fear: feeling suspicious or afraid of danger, threat, evil or pain; horror
    "A person feeling suspicious or afraid of danger, threat, or pain in a threatening environment.",
    # 16 - Happiness: feeling delighted; feeling enjoyment or amusement
    "A person feeling delighted, showing enjoyment or amusement in a pleasant context.",
    # 17 - Pain: physical suffering
    "A person experiencing physical suffering and bodily distress.",
    # 18 - Peace: well being and relaxed; no worry; having positive thoughts or sensations; satisfied
    "A person in a state of well-being, relaxed and satisfied with no worry in a calm environment.",
    # 19 - Pleasure: feeling of delight in the senses
    "A person experiencing delight in the senses, savoring a pleasurable moment.",
    # 20 - Sadness: feeling unhappy, sorrow, disappointed, or discouraged
    "A person feeling unhappy, sorrowful, disappointed, or discouraged in their surroundings.",
    # 21 - Sensitivity: feeling of being physically or emotionally wounded; feeling delicate or vulnerable
    "A person feeling physically or emotionally wounded, appearing delicate and vulnerable.",
    # 22 - Suffering: psychological or emotional pain; distressed; anguished
    "A person in psychological or emotional pain, appearing distressed and anguished.",
    # 23 - Surprise: sudden discovery of something unexpected
    "A person reacting to a sudden discovery of something unexpected in their environment.",
    # 24 - Sympathy: state of sharing others emotions, goals or troubles; supportive; compassionate
    "A person sharing in another's emotions or troubles, being supportive and compassionate.",
    # 25 - Yearning: strong desire to have something; jealous; envious; lust
    "A person with a strong desire to have something, showing longing, envy, or intense wanting.",
]

# Prompt Ensemble: 5 prompts per class, focused on BODY POSTURE + SCENE CONTEXT
# (Optimized for 2-stream body+context architecture, no facial features mentioned)
prompt_ensemble_emotic_paper = [
    [   # 0 - Affection
        "A person showing fond feelings and tenderness, embracing or leaning close to someone in a warm setting.",
        "A person holding hands or hugging another with visible love and care in their environment.",
        "A scene of physical closeness where a person gently touches or holds someone with deep fondness.",
        "A person displaying love through intimate body contact in a comfortable, warm context.",
        "A tender interaction between people, with one person showing affection through gentle posture and closeness.",
    ],
    [   # 1 - Anger
        "A person showing intense displeasure with clenched fists, rigid body, and aggressive posture in a tense scene.",
        "A furious person in a confrontational stance, body language radiating rage and resentment.",
        "A person expressing intense anger through hostile body movements in a conflict situation.",
        "An enraged individual with tense muscles and aggressive gestures in a heated environment.",
        "A person displaying fury with a rigid, combative posture amid a tense, hostile scene.",
    ],
    [   # 2 - Annoyance
        "A person appearing bothered and irritated, with crossed arms and impatient posture in a frustrating situation.",
        "A frustrated person showing mild displeasure through dismissive body language in their surroundings.",
        "A person looking irritated and impatient, bothered by something or someone nearby.",
        "An impatient individual with restless, agitated body movements in an annoying environment.",
        "A person showing visible frustration through tense shoulders and fidgety hands in a bothersome scene.",
    ],
    [   # 3 - Anticipation
        "A person leaning forward in their seat, alert and prepared for something that is about to happen.",
        "An expectant individual with an attentive posture, hoping and looking forward to a future event.",
        "A person with a ready, alert stance, watching eagerly as they prepare for what comes next.",
        "A person in a state of preparation and readiness, body positioned forward with focused attention.",
        "An individual poised and waiting with visible hope and expectation in an active scene.",
    ],
    [   # 4 - Aversion
        "A person recoiling and turning their body away from something disgusting or repulsive in the scene.",
        "A person pulling back with defensive body language, showing strong dislike toward something nearby.",
        "An individual shielding themselves or stepping back from an unpleasant stimulus in their environment.",
        "A person displaying physical repulsion, body turned away from a source of disgust or hate.",
        "A person with averted body posture and protective gestures in response to something revolting.",
    ],
    [   # 5 - Confidence
        "A person standing tall with an upright posture, exuding certainty and pride in their surroundings.",
        "A self-assured individual walking with purpose, body language showing conviction and encouragement.",
        "A person displaying confidence through a composed, commanding posture in a favorable setting.",
        "A proud person with an open, assured stance, clearly feeling certain about a positive outcome.",
        "An individual radiating self-belief with a powerful, relaxed posture in their environment.",
    ],
    [   # 6 - Disapproval
        "A person with a hostile posture, showing contempt and the feeling that something is wrong.",
        "An individual displaying moral disapproval through stern body language and judgmental stance.",
        "A person showing reprehension with crossed arms and a rigid, hostile posture toward something.",
        "A person conveying contempt and disapproval through cold, critical body language in the scene.",
        "An individual expressing that something is reprehensible through dismissive, hostile gestures.",
    ],
    [   # 7 - Disconnection
        "A person sitting alone, turned away from the main activity, appearing bored and indifferent.",
        "A distracted individual not engaged with their surroundings, body language showing disinterest.",
        "A person appearing detached from the main event, looking away with an indifferent posture.",
        "An isolated person in a group setting, body turned inward showing boredom and disconnection.",
        "A person physically present but mentally absent, with a distracted, uninterested posture.",
    ],
    [   # 8 - Disquietment
        "A nervous person with tense body language, appearing worried and anxious in an unsettling scene.",
        "A person showing visible anxiety through restless movements, tense posture, and alarmed behavior.",
        "An upset individual fidgeting with pressured, tense body language in a stressful environment.",
        "A worried person pacing or shifting nervously, body visibly tense and anxious.",
        "A person displaying alarm and unease through hunched shoulders and nervous gestures in a tense setting.",
    ],
    [   # 9 - Doubt/Confusion
        "A person in a state of uncertainty, body language showing hesitation and difficulty deciding.",
        "A confused individual scratching their head or pausing, unable to understand the situation.",
        "A person looking around with hesitant movements, clearly thinking about different options.",
        "An individual displaying confusion through uncertain gestures and a puzzled, indecisive posture.",
        "A person having difficulty understanding what is happening, body language showing doubt and hesitation.",
    ],
    [   # 10 - Embarrassment
        "A person looking down with hunched shoulders, feeling ashamed in front of others.",
        "A guilty-looking individual trying to hide or make themselves smaller in an awkward social scene.",
        "A person covering their body or turning away, showing visible shame and self-consciousness.",
        "An embarrassed person with a shrinking posture, avoiding attention from people around them.",
        "A person displaying guilt and shame through withdrawn, awkward body language in a social setting.",
    ],
    [   # 11 - Engagement
        "A person paying full attention to an activity, body leaned forward with absorbed, curious posture.",
        "An interested individual fully immersed in a task, showing deep concentration through their body language.",
        "A person actively participating in something, body language showing curiosity and complete absorption.",
        "A person showing engagement through alert, focused posture and active involvement in an activity.",
        "An absorbed individual with attentive body positioning, deeply interested in what is happening.",
    ],
    [   # 12 - Esteem
        "A person showing respect and admiration toward someone, with an approving and grateful posture.",
        "An individual clapping or nodding with visible admiration, showing favorable judgment of another.",
        "A person displaying gratefulness and respect through warm, attentive body language toward someone.",
        "A person showing high regard for another through a respectful stance and gestures of recognition.",
        "An admiring individual expressing favorable opinion through supportive body language and posture.",
    ],
    [   # 13 - Excitement
        "A person bursting with enthusiasm, body full of energy with dynamic, stimulated movements.",
        "An energetic individual jumping, cheering, or moving rapidly with visible stimulation and thrill.",
        "A person showing excitement through animated, high-energy body movements in a lively scene.",
        "A stimulated person with enthusiastic gestures and an energetic posture in an active environment.",
        "An individual radiating enthusiasm and energy through explosive, dynamic body language.",
    ],
    [   # 14 - Fatigue
        "A weary person with a slumped, tired posture, showing signs of sleepiness and exhaustion.",
        "A sleepy individual barely keeping upright, body drooping with visible tiredness.",
        "A person showing weariness through slow, lethargic body movements and a slouched position.",
        "A fatigued individual resting or leaning heavily, body language expressing complete tiredness.",
        "A tired person yawning or closing their eyes, body slumped with exhaustion in a quiet setting.",
    ],
    [   # 15 - Fear
        "A person in a threatening environment, body frozen or cowering with suspicion and dread of danger.",
        "A scared individual with a defensive posture, body tense and rigid, afraid of a threat or pain.",
        "A person showing horror and fear through a cowering, protective stance in a dangerous scene.",
        "A terrified person backing away from something evil or threatening with panicked body language.",
        "An afraid individual with rigid, protective body positioning in a dark, threatening environment.",
    ],
    [   # 16 - Happiness
        "A delighted person with relaxed body language, showing enjoyment and amusement in a pleasant scene.",
        "A person expressing joy through light, open body posture in a comfortable, happy environment.",
        "A happy individual showing visible delight and amusement through relaxed, carefree body language.",
        "A person radiating enjoyment in a pleasant setting, body open and relaxed with contentment.",
        "A delighted person in a bright, positive environment, body language showing pure enjoyment.",
    ],
    [   # 17 - Pain
        "A person experiencing physical suffering, clutching or protecting an injured part of their body.",
        "An individual in visible physical distress, body contorted and tense from physical pain.",
        "A person doubled over or holding themselves, showing clear signs of bodily suffering.",
        "A person grimacing and guarding their body from physical pain in a distressing situation.",
        "An individual showing acute physical suffering through protective, strained body positioning.",
    ],
    [   # 18 - Peace
        "A relaxed person in a calm environment, body at rest with well-being and no visible worry.",
        "A satisfied individual sitting or lying peacefully, body language showing complete relaxation.",
        "A person in a serene, quiet setting, body relaxed and posture showing positive sensations.",
        "A person radiating well-being and satisfaction, body fully relaxed in a peaceful environment.",
        "An individual at peace with their surroundings, body still and comfortable with no tension.",
    ],
    [   # 19 - Pleasure
        "A person experiencing delight through their senses, body relaxed and savoring a pleasant moment.",
        "An individual showing sensory pleasure through a comfortable, indulgent posture and relaxed body.",
        "A person visibly enjoying a sensory experience, body language showing delight and gratification.",
        "A person savoring a pleasurable moment, body leaned back in comfort and sensory satisfaction.",
        "An individual in a state of sensory delight, body relaxed and fully enjoying the moment.",
    ],
    [   # 20 - Sadness
        "A person with a slumped, withdrawn posture, showing unhappiness and sorrow in their surroundings.",
        "A discouraged individual with bowed body and drooping shoulders, visibly disappointed.",
        "A person showing grief and sorrow through a collapsed, withdrawn body position in a gloomy setting.",
        "An unhappy person sitting alone with defeated posture, body language showing deep disappointment.",
        "A sorrowful individual with a heavy, drooping body, showing visible discouragement in a somber scene.",
    ],
    [   # 21 - Sensitivity
        "A person appearing emotionally wounded and vulnerable, body language showing delicacy and openness.",
        "A vulnerable individual with a delicate posture, visibly affected physically or emotionally.",
        "A person displaying emotional sensitivity through fragile, exposed body language in a touching scene.",
        "A delicate person with open, vulnerable body positioning, appearing physically or emotionally wounded.",
        "An individual showing sensitivity through trembling or guarded body language, appearing fragile.",
    ],
    [   # 22 - Suffering
        "A distressed person showing psychological or emotional pain through anguished body language.",
        "An individual in visible anguish, body hunched and strained under emotional or psychological distress.",
        "A person enduring emotional suffering, body collapsed or tense with visible distress and torment.",
        "A person showing deep anguish through a broken, defeated posture in a harsh environment.",
        "An anguished individual displaying psychological pain through strained, tormented body language.",
    ],
    [   # 23 - Surprise
        "A person reacting to something unexpected, body jerking or freezing in sudden discovery.",
        "An individual caught off guard by a sudden event, body startled with unexpected movements.",
        "A person showing surprise through abrupt body reactions to an unexpected discovery in the scene.",
        "A startled person with sudden, involuntary body movement in response to something unforeseen.",
        "An individual reacting to an unexpected situation with a suddenly frozen or recoiling body.",
    ],
    [   # 24 - Sympathy
        "A compassionate person reaching out to comfort another, body language showing support and shared emotion.",
        "A person leaning toward someone in trouble, body positioned to offer support and understanding.",
        "A supportive individual with gentle, caring body language, sharing in another person's difficulties.",
        "A person showing compassion through physical closeness and supportive posture toward someone troubled.",
        "A compassionate individual with open, caring body language, visibly sharing another's emotional state.",
    ],
    [   # 25 - Yearning
        "A person gazing longingly with a tense, reaching posture, showing a strong desire for something.",
        "An individual with body leaned forward or reaching out, expressing envy or intense longing.",
        "A person displaying strong desire through a wistful, tense posture directed at something distant.",
        "A longing person with a restless, yearning body position, clearly wanting something they cannot have.",
        "An individual showing jealousy or intense desire through a tense, forward-leaning body stance.",
    ],
]

# =============================================================================
# COMBINED: Paper Definitions + Body+Context Prompts (7 per class)
# =============================================================================
# For each class:
#   [0] Paper definition (Kosti et al., TPAMI 2019, Table 1) — formal/academic
#   [1] Creative descriptor (rich visual cues) — face+body+context
#   [2-6] Body+context prompts — body posture + scene context (no face)
#
# This gives the model 3 complementary perspectives:
#   1. Academic grounding from the official definition
#   2. Rich multimodal visual cues
#   3. Body+context focused descriptions for the 2-stream architecture

prompt_ensemble_emotic_combined = [
    [class_descriptor_emotic_paper[i]] + [class_descriptor_emotic[i]] + prompt_ensemble_emotic_paper[i]
    for i in range(26)
]
