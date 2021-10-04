# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO PRINT EMOJIS USING EMOJI MODULE, UNICODE CHARACTERS & CLDR NAMES
#
# EMOJIS can be printed with the help of the emojis module of Python.
#
# The module can be installed by using the command - pip install emoji

# ------------------------------PRINTING EMOJIS USING emoji MODULE----------------------------

# Importing the emoji module
import emoji

# -----------------------------PRINTING EMOJIS USING emojize()----------------------------------

# emojize() function is used to convert the CLDR short name to the corresponding emoji
# which takes the CLDR name as the argument. Replace the underscores in the name with
# the underscores

print("\nPRINTING EMOJIS USING emojize() FUNCTION OF emoji MODULE\n")
print("WINKING FACE WITH TONGUE         : ", emoji.emojize(":winking_face_with_tongue:"))
print("GRINNING FACE WITH BIG EYES      : ", emoji.emojize(":grinning_face_with_big_eyes:"))
print("BEAMING FACE WITH SMILING EYES   : ", emoji.emojize(":beaming_face_with_smiling_eyes:"))
print("SMILING FACE WITH SMILING EYES   : ", emoji.emojize(":smiling_face_with_smiling_eyes:"))
print("SMILING FACE WITH HALO           : ", emoji.emojize(":smiling_face_with_halo:"))

# --------------------------PRINTING CLDR SHORT USING demojize()-------------------------------

# emojize() function is used to convert the CLDR short name to the corresponding emoji
# which takes the CLDR name as the argument. Replace the underscores in the name with
# the underscores

print("\n\nPRINTING CLDR SHORT NAME OF EMOJIS USING demojize() OF emoji MODULE\n")
print("😂 - ", emoji.demojize("😂"))
print("🤪 - ", emoji.demojize("🤪"))
print("😎 - ", emoji.demojize("😎"))
print("😄 - ", emoji.demojize("😄"))
print("😅 - ", emoji.demojize("😅"))

# ---------------------------PRINTING EMOJIS USING UNICODE CHARACTERS-------------------------

# Emojis can also be printed using the UNICODE characters

print("\n\nPRINTING EMOJIS USING THE UNICODE CHARACTERS\n")
print("THINKING FACE            : ", "\U0001F914")
print("ZIPPER-MOUTH FACE        : ", "\U0001F910")
print("FACE WITH RAISED EYEBROW : ", "\U0001F928")
print("NEUTRAL FACE             : ", "\U0001F610")
print("SMIRKING FACE            : ", "\U0001F60F")

# ----------------------------PRINTING EMOJIS USING CLDR SHORT NAMES--------------------------

# Emojis can also be printed using the CLDR SHORT NAME

print("\n\nPRINTING EMOJIS USING CLDR SHORT NAMES\n")
print("HUGGING FACE             : ", "\N{hugging face}")
print("FACE WITH ROLLING EYES   : ", "\N{face with rolling eyes}")
print("RELIEVED FACE            : ", "\N{relieved face}")
print("SLEEPING FACE            : ", "\N{sleeping face}")
print("DROOLING FACE            : ", "\N{drooling face}")
