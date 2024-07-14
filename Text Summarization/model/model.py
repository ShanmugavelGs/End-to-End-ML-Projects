from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summarizer.save_pretrained('D:\Project Files\Hugging Face\Text Summarization\model')