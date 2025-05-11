from craftyai import CraftyAI

openai_api_key = "hf_MeCCVRPbvwhhvEgGdXZHKUZVqEjNQjNPJMm"

craftyai = CraftyAI(
    openai_api_key=openai_api_key,
    mc_port=51146,
    resume=False,
)

task = "Craft furnace"
sub_goals = craftyai.decompose_task(task=task)

craftyai.inference(sub_goals=sub_goals)
craftyai.learn()