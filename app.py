import random
import streamlit as st

# Define categorized prompt components
realism_keywords = [
    "Kodak Portra 400", "Fujifilm XT3 Provia 100F", "Screenshot from Criterion Collection film",
    "Behind the scenes on set of Blade Runner 2049", "Scanned from a 1995 Vogue magazine"
]

photorealism_keywords = [
    "Shot on Canon EOS R5 + Sigma Art lens, F1.4, bokeh", "Taken from Google Street View, blurry background",
    "Nikon D850, RAW unedited file, ISO 100", "Photographed for a Time Magazine cover story",
    "CCTV surveillance footage, 1997 Japan"
]

artistic_keywords = [
    "Styled by IKEA catalog 2007", "MoMA exhibit scan", "Archived editorial from National Geographic, 1984",
    "Album cover designed by Storm Thorgerson"
]

data_keywords = [
    "Scanned from DeviantArt portfolio, 2006", "Concept sheet by Pixar pre-production",
    "Uploaded to Behance, 2012, layout study", "Generated by NASA training dataset"
]

magic_keywords = [
    "ArtStation HQ render", "Volumetric lighting, cinematic shadows, global illumination",
    "Color-graded by Roger Deakins", "Captured for Getty Images editorial use",
    "Hyperreal sketchbook study by Da Vinci, graphite on vellum"
]

video_keywords = [
    "4K slow motion cinematic reel", "Drone flyover footage, sweeping camera pan",
    "Hyperlapse footage of futuristic city", "Tracking shot with shallow depth of field",
    "Opening sequence of a sci-fi short film"
]

bonus_templates = [
    "Shot from {camera} with {lens}, ISO {iso}, aperture {aperture}, using {film}",
    "Archived footage from {place}, {year}, used for {purpose}",
    "Design layout inspired by {design_house}"
]

bonus_options = {
    "camera": ["Canon EOS R6", "Sony A7R IV", "Nikon Z9"],
    "lens": ["Sigma 35mm F1.4", "Canon RF 85mm F1.2", "Sony Zeiss 50mm F1.8"],
    "iso": ["100", "400", "800"],
    "aperture": ["F1.2", "F1.4", "F2.8"],
    "film": ["Kodak Gold 200", "Fujicolor Superia X-TRA 400", "Ilford HP5 Plus 400"],
    "place": ["Tokyo", "New York", "Paris"],
    "year": ["1997", "1984", "2001"],
    "purpose": ["news coverage", "surveillance", "art documentary"],
    "design_house": ["Pentagram", "Sagmeister & Walsh", "IDEO"]
}

def generate_prompt(include_video=False):
    section = random.choice([
        realism_keywords, photorealism_keywords, artistic_keywords,
        data_keywords, magic_keywords
    ])

    if include_video:
        section += video_keywords

    main_keyword = random.choice(section)
    template = random.choice(bonus_templates)

    filled_template = template.format(
        camera=random.choice(bonus_options["camera"]),
        lens=random.choice(bonus_options["lens"]),
        iso=random.choice(bonus_options["iso"]),
        aperture=random.choice(bonus_options["aperture"]),
        film=random.choice(bonus_options["film"]),
        place=random.choice(bonus_options["place"]),
        year=random.choice(bonus_options["year"]),
        purpose=random.choice(bonus_options["purpose"]),
        design_house=random.choice(bonus_options["design_house"])
    )

    return f"{main_keyword}, {filled_template}"

# Streamlit App Interface
st.title("AI Art Prompt Generator")
st.markdown("Generate ultra-creative AI prompts using hidden and powerful keywords. Choose to generate prompts for still images or video scenes.")

video_mode = st.checkbox("🎥 Enable Video-Style Prompt")

if st.button("🎨 Generate Prompt"):
    generated_prompt = generate_prompt(include_video=video_mode)
    user_prompt = st.text_area("📝 Customize Your Prompt Below:", generated_prompt, height=200)
    st.markdown("### ✅ Final Prompt:")
    st.code(user_prompt, language='markdown')
    st.download_button("📥 Download Prompt as Text", user_prompt, file_name="ai_prompt.txt")
