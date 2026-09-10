import re

with open('app/src/main/java/com/example/ui/ChatViewModel.kt', 'r') as f:
    text = f.read()

# Make sure to import Tool and GoogleSearch
imports = """import com.example.api.Tool
import com.example.api.GoogleSearch
import"""
text = text.replace('import', imports, 1)

# Modify GenerateContentRequest initialization
old_req = """                val request = GenerateContentRequest(
                    contents = contents,
                    systemInstruction = systemInstruction
                )"""

new_req = """                val request = GenerateContentRequest(
                    contents = contents,
                    systemInstruction = systemInstruction,
                    tools = listOf(Tool(googleSearch = GoogleSearch()))
                )"""

text = text.replace(old_req, new_req)

with open('app/src/main/java/com/example/ui/ChatViewModel.kt', 'w') as f:
    f.write(text)
print("Patched ChatViewModel.kt")
