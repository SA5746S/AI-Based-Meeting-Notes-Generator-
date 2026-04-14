from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Stable model (VERY IMPORTANT)
model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def summarize_text(text):
    if not text or len(text) < 50:
        return text

    prompt = "Summarize the following meeting notes:\n" + text

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    output = model.generate(
        **inputs,
        max_length=150,
        min_length=40,
        num_beams=4
    )

    summary = tokenizer.decode(output[0], skip_special_tokens=True)

    return summary