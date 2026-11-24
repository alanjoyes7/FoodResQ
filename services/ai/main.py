import os
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from openai import OpenAI
app=FastAPI(title="FoodResQ AI Assistance")
class Listing(BaseModel): food_name:str=Field(min_length=2,max_length=120);notes:str=""
@app.get("/health")
def health():return {"status":"ok","service":"foodresq-ai"}
@app.post("/assist/listing")
def assist(data:Listing):
 if not os.getenv("OPENAI_API_KEY"):raise HTTPException(503,"AI assistance is not configured")
 prompt=("Suggest an editable category from cooked_meals, bakery, fruits, vegetables, packaged, dairy; description and tags. Never infer freshness, contamination, allergens or safety. Return JSON. Food: "+data.food_name+" Notes: "+data.notes)
 try:
  out=OpenAI().chat.completions.create(model=os.getenv("OPENAI_MODEL","gpt-4o-mini"),messages=[{"role":"user","content":prompt}],response_format={"type":"json_object"})
  return {"suggestion":out.choices[0].message.content,"editable":True,"disclaimer":"AI cannot certify food safety or freshness."}
 except Exception as exc:raise HTTPException(502,"AI provider request failed") from exc
