from deep_translator import GoogleTranslator
t=GoogleTranslator(
    source="auto",
    target="en"
)
w=input("enter something:")
r=t.translate(w)
print(f"{w} is {r} right?")