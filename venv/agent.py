import os
from dotenv import load_dotenv
from livekit.plugins import google
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import noise_cancellation

load_dotenv(".env.local")

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a helpful voice AI assistant.")

async def entrypoint(ctx: agents.JobContext):
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables")

    session = AgentSession(
        llm=google.realtime.RealtimeModel(
            model="gemini-2.0-flash-exp",
            voice="Puck",
            temperature=0.8,
            instructions="You are a helpful assistant",
            api_key=api_key,  # explicitly pass API key here
        ),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await session.generate_reply(
        instructions="Greet the user and offer your assistance. You should start by speaking in English."
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
