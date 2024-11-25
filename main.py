import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero

load_dotenv()

async def entrypoint(ctx: JobContext):
   initial_ctx = llm.ChatContext().append(
       role="system",
       text=(
           "Greetings, I am your Voice Navigator, crafted by the innovators at LiveKit. "
           "My realm is the spoken word, where I weave responses with wit and brevity. "
           "I shun the complex, embracing only the most articulate and clear expressions, "
           "ensuring our conversation flows like a well-composed melody."
       ),
   )
   
   await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
   
   assistant = VoiceAssistant(
       vad=silero.VAD.load(),
       stt=openai.STT(),
       llm=openai.LLM(),
       tts=openai.TTS(),
       chat_ctx=initial_ctx,
   )
   
   assistant.start(ctx.room)
   await asyncio.sleep(1)
   await assistant.say("Hey, how can I assist you today!", allow_interruptions=True)

if __name__ == "__main__":
   cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
