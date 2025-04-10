import random
import streamlit as st

# Initialize session state
if "prompt_history" not in st.session_state:
    st.session_state.prompt_history = []

# Define upscale-style categories
upscale_categories = {
    "None": "",
    "Food - Fruits & Veggies": "hyper-detailed skin texture, fresh glistening surface, vibrant colors, crisp clarity",
    "Food - Meat & Fried": "crispy surface, sizzling texture, golden crust, oil glisten, ultra-sharp detail",
    "Food - Beverages": "condensation droplets, smooth glass reflection, vivid color gradients, ultra-refresh",
    "People - High Resolution": "ultra-sharp focus on facial details, cinematic lighting on skin, fine hair strands",
    "People - Black & White": "grain-free monochrome, sharp shadows, contrasty lighting, timeless film grain",
    "People - 80s Style": "soft retro focus, pastel highlights, vintage grain, Polaroid texture",
    "People - 90s Style": "Kodak Gold tones, natural skin exposure, crisp fashion details",
    "Cars - Glossy & Wet": "shiny surface, water reflections, showroom polish, ambient light refraction",
    "Cars - Race Ready": "carbon fiber reflections, detailed tire texture, motion blur in background"
}

pose_keywords = [
    "standing still with intense gaze", "mid-step walking motion",
    "arms crossed confidently", "hands behind back in relaxed posture",
    "reaching out toward the viewer", "dancing with movement in dress",
    "kneeling by a pond", "sitting on stone ledge"
]

species_keywords = [
    "elf", "mermaid", "cyborg", "vampire", "centaur", "dragonborn", "fairy", "demon", "alien", "android"
]

camera_angle_keywords = [
    "overhead drone shot", "low angle shot", "high angle close-up", "POV handheld", "macro extreme close-up", "360-degree panoramic"
]

# App UI

# Power Prompt Mode toggle
power_mode = st.checkbox("⚡ Power Prompt Mode (show advanced options)")
if st.button("🔀 Randomize All Fields"):
    import random
    gender = random.choice(["man", "woman", "nonbinary"])
    age = random.choice(["child", "teen", "20s", "30s", "40s", "50s", "senior"])
    body_type = random.choice(["slim", "athletic", "curvy", "plus-size", "muscular", "petite", "voluptuous", "toned", "modelesque"])
    setting = random.choice(["urban", "nature", "futuristic", "vintage", "studio", "temple ruins", "cherry blossom grove"])
    mood = random.choice(["happy", "sad", "mysterious", "epic", "romantic", "melancholy", "elegant", "dreamy"])
    camera_angle = random.choice(camera_angle_keywords)
    clothing = random.choice(["casual", "formal", "evening gown", "cyberpunk gear", "athletic wear", "lace dress", "bikini", "warrior costume"])
    pose = random.choice(pose_keywords)
    species = random.choice(species_keywords)
    upscale_choice = random.choice(list(upscale_categories.keys())[1:])  # skip "None"
    upscale_addition = upscale_categories[upscale_choice]
    subject_input = random.choice(["A lone samurai in the mist", "A glistening bowl of fruit", "A futuristic knight on a hover bike"])
    style_input = random.choice(["filmic lighting, 35mm lens", "shot on Canon EOS R5", "hyperreal rendering with Octane"])

st.title("AI Art Prompt Generator 🎨")
st.markdown("Craft ultra-detailed prompts with cinematic enhancements, styled by subject.")

# Main controls
gender = st.selectbox("🚻 Gender:", ["", "man", "woman", "nonbinary"])
age = st.selectbox("📅 Age:", ["", "child", "teen", "20s", "30s", "40s", "50s", "senior"])
body_type = st.selectbox("🏋️ Body Type:", ["", "slim", "athletic", "curvy", "plus-size", "muscular", "petite", "voluptuous", "toned", "modelesque"])
setting = st.selectbox("🌍 Scene/Setting:", ["", "urban", "nature", "futuristic", "vintage", "studio", "temple ruins", "cherry blossom grove"])
mood = st.selectbox("🎭 Mood:", ["", "happy", "sad", "mysterious", "epic", "romantic", "melancholy", "elegant", "dreamy"])
camera_angle = st.selectbox("🎥 Camera Angle:", ["", *camera_angle_keywords])
clothing = st.selectbox("👗 Clothing:", ["", "casual", "formal", "evening gown", "cyberpunk gear", "athletic wear", "lace dress", "bikini", "warrior costume"])
pose = st.selectbox("🧍 Pose:", ["", *pose_keywords])
species = st.selectbox("🧬 Fantasy Species:", ["", *species_keywords])

# Upscale enhancement
upscale_choice = st.selectbox("🆙 Optional: Add Upscale Prompt Based on Subject", list(upscale_categories.keys()))
upscale_addition = upscale_categories[upscale_choice]

# Subject + style text input
subject_input = st.text_input("🖼 Describe your subject:", "A beautiful futuristic warrior")
style_input = st.text_input("🎨 Style keywords (optional):", "shot on Canon EOS R5, volumetric lighting")

# Power Prompt Fields
if power_mode:
    negative_prompt_toggle = st.checkbox("🚫 Add Negative Prompt (Power Mode)")
    lighting = st.selectbox("💡 Lighting Style:", ["", "golden hour", "neon glow", "rim lighting", "chiaroscuro", "studio softbox"])
    render_engine = st.selectbox("🧪 Render Engine:", ["", "Octane", "Unreal Engine 5", "Redshift", "Cinema4D"])
    composition = st.selectbox("🎞️ Composition Style:", ["", "rule of thirds", "Dutch angle", "top-down view", "over-the-shoulder"])
    aesthetic = st.selectbox("🖼️ Aesthetic Style:", ["", "fashion editorial", "photojournalism", "fine art museum grade", "surrealist"])
    tech = st.selectbox("⚙️ Technical Enhancements:", ["", "32-bit HDR", "ray tracing", "zero chromatic aberration", "DCI-P3 color calibration"])
else:
    negative_prompt_toggle = False
    lighting = render_engine = composition = aesthetic = tech = ""
if st.button("✨ Generate Prompt"):
    power_parts = []
    if lighting: power_parts.append(f"lit with {lighting}")
    if render_engine: power_parts.append(f"rendered in {render_engine}")
    if composition: power_parts.append(f"composition: {composition}")
    if aesthetic: power_parts.append(aesthetic)
    if tech: power_parts.append(tech)
    prompt_parts = []

    if age:
        prompt_parts.append(f"{age} year old")
    if gender:
        prompt_parts.append(gender)
    if species:
        prompt_parts.append(species)
    if body_type:
        prompt_parts.append(f"with a {body_type} body type")
    if clothing:
        prompt_parts.append(f"wearing {clothing}")
    if setting:
        prompt_parts.append(f"in a {setting} setting")
    if mood:
        prompt_parts.append(f"capturing a {mood} mood")
    if camera_angle:
        prompt_parts.append(f"shot from a {camera_angle}")
    if pose:
        prompt_parts.append(f"posed {pose}")

    description = ", ".join(prompt_parts)
    base_prompt = f"{subject_input.strip()}, {description}, {style_input.strip()}"

    if upscale_addition:
        base_prompt += ", " + upscale_addition
    if power_parts:
        base_prompt += ", " + ", ".join(power_parts)
    if negative_prompt_toggle:
       base_prompt += "\n\nNegative Prompt: blurry, low-res, bad anatomy, deformed, extra limbs, watermark, cropped, noisy, text"


    st.session_state.prompt_history.insert(0, base_prompt.strip())
    st.markdown("### ✅ Your Final Prompt")
    st.code(base_prompt.strip(), language='markdown')
    st.download_button("📥 Download Prompt as Text", base_prompt.strip(), file_name="ai_prompt.txt")

# Prompt history
if st.session_state.prompt_history:
    st.markdown("### 🕓 Prompt History")
    for i, past in enumerate(st.session_state.prompt_history[:10], 1):
        st.markdown(f"**{i}.** {past}")

# Footer
st.markdown("---")
st.markdown("☕️ Enjoying this tool? [Buy Me a Coffee](https://www.buymeacoffee.com/yourusername) ❤️")
