import streamlit as st
from pathlib import Path
from urllib.parse import quote

st.set_page_config(
    page_title="SKY BLUE INDUSTRIES",
    page_icon="🏭",
    layout="wide"
)

# Company heading
st.title("🏭 SKY BLUE INDUSTRIES")
st.subheader("Quality Plastic Products")
st.write(
    "Welcome to SKY BLUE INDUSTRIES! "
    "Explore our products and contact us for enquiries."
)

st.divider()

# WhatsApp number: India country code + your number
PHONE_NUMBER = "919961610321"

# Published products
products = [
    {
        "name": "Goat Mat",
        "image": "goat_mat.png",
        "description": "Plastic mat for goat farming.",
        "price": 140,
        "size": "2 × 1 ft"
    },
    {
        "name": "Heavy Goat Mat",
        "image": "heavy_goat_mat.png",
        "description": "Heavy-duty plastic mat for goat farming.",
        "price": 200,
        "size": "2 × 1 ft"
    },
    {
        "name": "Jumbo Fridge Stand",
        "image": "jumbo_stand.png",
        "description": "Durable plastic fridge stand.",
        "price": 175,
        "size": "Contact us for details"
    }
]

st.header("🛍️ Our Products")

image_folder = Path(__file__).parent / "images"
columns = st.columns(3)

for index, product in enumerate(products):
    with columns[index]:
        st.subheader(product["name"])

        image_path = image_folder / product["image"]

        if image_path.exists():
            st.image(str(image_path), use_container_width=True)
        else:
            st.warning(f"Image not found: {product['image']}")

        st.write(product["description"])
        st.write(f"**Price: ₹{product['price']}**")
        st.write(f"**Size: {product['size']}**")

        message = (
            f"Hello SKY BLUE INDUSTRIES! "
            f"I am interested in the {product['name']}. "
            f"Please share more details."
        )

        whatsapp_url = (
            f"https://wa.me/{PHONE_NUMBER}"
            f"?text={quote(message)}"
        )

        st.link_button(
            "📲 Enquire on WhatsApp",
            whatsapp_url,
            key=f"whatsapp_{index}"
        )

st.divider()

st.header("📞 Contact Us")
st.write("For product enquiries, contact SKY BLUE INDUSTRIES.")

general_message = quote(
    "Hello SKY BLUE INDUSTRIES! I would like to know more about your products."
)

st.link_button(
    "💬 Chat with Us on WhatsApp",
    f"https://wa.me/{PHONE_NUMBER}?text={general_message}"
)

st.caption("© SKY BLUE INDUSTRIES")

