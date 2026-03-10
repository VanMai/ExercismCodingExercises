def translate(text):
    words = text.split()
    translated_words = []
    vowels = "aeiou"
    
    for word in words:
        # Rule 1: Vowel start or special combinations
        if word[0] in vowels or word.startswith(("xr", "yt")):
            translated_words.append(word + "ay")
        
        # Rules 2, 3, 4: Consonant clusters, 'qu', 'y'
        else:
            # Find the position of the first vowel, treating 'qu' as a unit
            consonant_cluster_len = 0
            for i, char in enumerate(word):
                if char in vowels or (char == 'y' and i > 0):
                    # Special case: 'qu'
                    if i > 0 and word[i-1:i+1] == "qu":
                        consonant_cluster_len = i + 1
                    else:
                        consonant_cluster_len = i
                    break
                elif i == len(word) - 1: # No vowels found
                    consonant_cluster_len = len(word)
            
            # Apply transformation
            prefix = word[:consonant_cluster_len]
            suffix = word[consonant_cluster_len:]
            translated_words.append(suffix + prefix + "ay")
            
    return " ".join(translated_words)
