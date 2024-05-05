import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models

def generate():
  vertexai.init(project="starry-antonym-422110-f7", location="us-central1")
  model = GenerativeModel("gemini-experimental")
  responses = model.generate_content(
      [text1, video1],
      generation_config=generation_config,
      safety_settings=safety_settings,
  )

  print(responses)

text1 = """Where this video was taken precise location of it according to the background and video give me exact coordinates etc. and give me more comprehensive information about the location"""
video1 = Part.from_data(
    mime_type="video/mp4",

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}

generate()
