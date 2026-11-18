def remove_filler(paragraph):
    """Removes punctuation and filler words from a complaint string."""
    # list of filler words to ignore
    IGNORE_WORDS = {
        "a", "an", "the", "this", "that", "these", "those", "my", "our", "your", "his", "her", "its", "their",
        "each", "every", "either", "neither", "both", "all", "some", "any", "many", "much", "few", "several",
        "most", "other", "another", "such", "certain", "particular", "i", "me", "myself", "we", "us", "ourselves",
        "you", "yourself", "yourselves", "he", "him", "himself", "she", "herself", "it", "itself", "they", "them",
        "themselves", "who", "whom", "whose", "which", "what", "whatever", "whoever", "whichever", "someone",
        "somebody", "something", "anyone", "anybody", "anything", "everyone", "everybody", "everything", "here",
        "there", "in", "on", "under", "at", "by", "for", "with", "about", "against", "between", "into", "through",
        "during", "before", "after", "above", "below", "to", "from", "of", "over", "beneath", "beside", "besides",
        "beyond", "inside", "outside", "near", "nearby", "onto", "upon", "within", "without", "across", "along",
        "around", "behind", "toward", "towards", "until", "till", "via", "per", "amid", "among", "throughout",
        "unlike", "regarding", "concerning", "am", "is", "are", "was", "were", "be", "been", "being", "have",
        "has", "had", "having", "do", "does", "did", "doing", "done", "will", "would", "shall", "should", "can",
        "could", "may", "might", "must", "ought", "and", "but", "or", "nor", "so", "yet", "because", "since",
        "although", "though", "while", "whereas", "if", "unless", "whether", "as", "than", "once", "when",
        "whenever", "where", "wherever", "why", "how", "however", "therefore", "thus", "hence", "moreover",
        "furthermore", "additionally", "also", "too", "nonetheless", "nevertheless", "meanwhile", "subsequently",
        "consequently", "accordingly", "regardless", "irrespective", "anyway", "basically", "actually", "literally",
        "honestly", "frankly", "seriously", "truthfully", "technically", "virtually", "essentially", "fundamentally",
        "practically", "generally", "typically", "usually", "normally", "mostly", "mainly", "largely", "partially",
        "somewhat", "fairly", "rather", "quite", "so-called", "now", "incidentally", "suppose", "imagine",
        "firstly", "secondly", "thirdly", "lastly", "finally", "maybe", "perhaps", "possibly", "probably",
        "presumably", "apparently", "seemingly", "supposedly", "allegedly", "evidently", "clearly", "obviously",
        "naturally", "undoubtedly", "definitely", "certainly", "surely", "absolutely", "completely", "utterly",
        "entirely", "wholly", "truly", "really", "very", "extremely", "incredibly", "just", "simply", "merely",
        "only", "even", "already", "again", "namely", "specifically", "particularly", "especially", "notably",
        "chiefly", "primarily", "solely", "etc", "roughly", "approximately", "yes", "indeed", "true", "exactly",
        "precisely", "far", "kindly", "please", "sometimes", "oftentimes", "often", "occasionally", "rarely",
        "seldom", "always", "ever", "forever", "constantly", "continually", "frequently", "repeatedly",
        "periodically", "eventually", "ultimately", "gradually", "suddenly", "immediately", "instantly",
        "presently", "currently", "nowadays", "somehow", "somewhere", "anywhere", "everywhere", "various",
        "numerous", "countless"
    }

    # Step 1: Convert the whole sentence to lowercase first
    paragraph = paragraph.lower()

    # Step 2: Remove basic punctuation marks
    for mark in {".", ",", "?", "!"}:
        paragraph = paragraph.replace(mark, "")

    # Step 3: Split the sentence into a list of individual words
    words = paragraph.split()

    # Step 4: Keep only the words that are NOT in IGNORE_WORDS
    clean_words = []
    for word in words:
        if word not in IGNORE_WORDS:
            clean_words.append(word)

    # Step 5: Join the kept words back into a single string separated by spaces
    return " ".join(clean_words)


def replace_words(paragraph):
    """Replaces synonym words with one standard keyword."""
    # Dictionary format -> "standard_word": ["synonym1", "synonym2", ...]
    synonyms = {
        # GENERAL COMPLAINTS
        "problem": ["issue", "trouble", "difficulty", "concern"],
        "complaint": ["grievance", "report", "objection"],
        "request": ["appeal", "demand", "application"],
        "delay": ["late", "postponement", "waiting"],
        "resolve": ["fix", "repair", "rectify", "solve"],
        "damage": ["broken", "faulty", "defective"],
        "unavailable": ["missing", "absent", "inaccessible"],
        "insufficient": ["inadequate", "limited", "scarce", "less"],
        "excessive": ["overly", "exorbitant"],

        # HOSTEL / ACCOMMODATION
        "hostel": ["dormitory", "residence", "dorm"],
        "room": ["accommodation", "quarters"],
        "student": ["resident", "boarder", "occupant"],
        "warden": ["superintendent", "caretaker"],
        "roommate": ["flatmate"],
        "bed": ["bunk"],
        "furniture": ["furnishing", "fixtures"],
        "cupboard": ["wardrobe", "closet", "cabinet"],
        "door": ["entrance"],
        "window": ["vent"],
        "lock": ["latch", "bolt"],

        # MAINTENANCE AND REPAIRS
        "maintenance": ["upkeep", "servicing"],
        "repair": ["fix", "mend", "restore"],
        "technician": ["mechanic", "repairman", "electrician"],
        "leak": ["leakage", "dripping"],
        "pipe": ["pipeline", "plumbing"],
        "drain": ["sewer", "outlet"],
        "clogged": ["blocked", "choked"],
        "broken": ["damaged", "faulty", "malfunctioning"],
        "crack": ["fracture", "split"],
        "ceiling": ["roof"],
        "wall": ["partition"],
        "fan": ["ventilator"],
        "light": ["lamp", "bulb", "lighting"],
        "socket": ["outlet"],
        "electricity": ["power"],
        "powercut": ["blackout", "outage"],

        # WATER AND BATHROOM
        "shortage": ["scarcity", "lack", "deficiency"],
        "supply": ["provision", "distribution"],
        "bathroom": ["washroom", "restroom", "toilet"],
        "toilet": ["lavatory", "washroom", "restroom"],
        "shower": ["bath"],
        "tap": ["faucet"],
        "geyser": ["heater"],
        "hot": ["heated", "warm"],
        "cold": ["chilled", "cool"],
        "smell": ["odour", "odor", "stench"],
        "dirty": ["unclean", "filthy", "soiled"],
        "wet": ["damp", "moist"],
        "hygiene": ["sanitation", "cleanliness"],

        # CLEANLINESS
        "clean": ["sanitary", "hygienic", "tidy"],
        "cleaning": ["sweeping", "mopping", "sanitation"],
        "cleaner": ["housekeeper"],
        "garbage": ["trash", "waste", "rubbish"],
        "mosquito": ["mosquitoes"],
        "insect": ["bug", "pest"],
        "pest": ["insect", "vermin"],
        "cockroach": ["roach"],
        "rat": ["rodent", "mouse"],
        "smelly": ["stinking"],

        # FOOD AND MESS
        "food": ["meal", "cuisine", "dish"],
        "mess": ["canteen", "cafeteria"],
        "dinner": ["supper"],
        "cook": ["chef"],
        "taste": ["flavour", "flavor"],
        "stale": ["spoiled", "rotten", "expired"],
        "spoiled": ["rotten", "decayed"],
        "undercooked": ["raw"],
        "overcooked": ["burnt", "burned"],
        "quantity": ["portion", "amount"],
        "quality": ["standard", "condition"],
        "hygienic": ["sanitary", "clean"],
        "oily": ["greasy"],
        "bland": ["tasteless", "flavourless"],
        "nutrition": ["nutrients"],

        # INTERNET AND TECHNOLOGY
        "internet": ["wifi", "wi-fi", "network", "connectivity"],
        "slow": ["sluggish", "laggy", "delayed"],
        "connection": ["connectivity", "network"],
        "disconnect": ["drop"],
        "signal": ["reception", "coverage"],
        "computer": ["pc", "system"],
        "access": ["availability", "entry"],

        # SECURITY
        "security": ["safety", "protection"],
        "guard": ["watchman"],
        "visitor": ["guest", "outsider"],
        "theft": ["stealing", "robbery"],
        "stolen": ["missing", "taken"],
        "surveillance": ["monitoring", "observation"],
        "camera": ["cctv"],
        "unsafe": ["dangerous", "insecure"],
        "restricted": ["prohibited", "forbidden"],

        # ADMINISTRATION
        "administration": ["management", "authorities", "office"],
        "permission": ["approval", "authorization"],
        "registration": ["enrollment", "enrolment"],
        "payment": ["fee", "charge", "dues"],
        "refund": ["reimbursement", "repayment"],
        "fine": ["penalty"],
        "rules": ["regulations", "guidelines"],
        "policy": ["regulation", "rule"],
        "staff": ["personnel", "employees", "workers"],
        "response": ["reply", "feedback"],
        "ignore": ["neglect", "overlook"],
        "unresponsive": ["uncooperative", "inattentive"],
        "notice": ["notification", "announcement"],
        "schedule": ["timetable", "roster"],
        "attendance": ["presence"],

        # ENVIRONMENT AND FACILITIES
        "noise": ["sound", "disturbance", "commotion"],
        "loud": ["noisy", "deafening"],
        "disturbance": ["disruption", "interference"],
        "quiet": ["silent", "peaceful"],
        "laundry": ["washing"],
        "washing": ["laundering"],
        "elevator": ["lift"],
        "stairs": ["staircase"],
        "corridor": ["hallway", "passage"],
        "gym": ["fitness"],

        # COMPLAINT SEVERITY
        "urgent": ["critical", "immediate", "emergency"],
        "frequent": ["repeated", "regular", "recurring"],
        "temporary": ["brief"],
        "permanent": ["lasting"],
        "severe": ["serious", "extreme"],
        "minor": ["small", "slight", "trivial"],
        "uncomfortable": ["inconvenient", "distressing"],
        "inconvenient": ["troublesome", "problematic"]
    }

    # Step 1: Split the cleaned sentence into a list of words
    words = paragraph.split()
    final_words = []

    # Step 2: Check each word against the synonym lists
    for word in words:
        new_word = word  # Default: keep the original word if no synonym matches

        for standard_word, synonym_list in synonyms.items():
            if word in synonym_list:
                new_word = standard_word  # Replace with the main dictionary key
                break

        final_words.append(new_word)

    # Step 3: Join the words back into a sentence and return it
    return " ".join(final_words)


def tuple_list_generator(complaint):
    """Generates a list of tuples containing the complaint and its weight"""
    pairs = []

    for i in range(len(complaint)):

        for j in range(i + 1, i + 6):  # Only consider pairs within a distance of 5 words

            distance = abs(j - i)
            weight = 1 / (distance * distance)  # Weight is inversely proportional to the square of the distance between words

            pairs.append((
                min(complaint[i],complaint[j]),
                max(complaint[i],complaint[j]),
                weight
            ))
    return pairs

def final_vector(word_pairs):
    """Generates a final vector representation of the complaint based on word pairs and their weights."""
    vector = []

    """do magic and figure out the vector based on a global list"""
    
    return vector


def search_algorithm_vector_generation(complaint):
    """Processes the complaint string by removing filler words and replacing synonyms."""
    cleaned_complaint = remove_filler(complaint)
    standardized_complaint = replace_words(cleaned_complaint)
    
    # Split the string into a list of words before passing it to the generator
    complaint_list = tuple_list_generator(standardized_complaint.split())
    
    final_vector_representation = final_vector(complaint_list)

    return final_vector_representation

    