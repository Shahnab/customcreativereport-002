import streamlit as st
from streamlit_image_comparison import image_comparison


st.set_page_config("Agumented Creative Optimizer", layout="wide")
st.image("logo.png", width=150)

##Sidebar
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Dentsu-logo_black.svg/2560px-Dentsu-logo_black.svg.png", width=100)
st.sidebar.header("Demo Creative Report")
st.sidebar.caption("Environment: Out of Home")
st.sidebar.subheader("ACO Creative Analyser Engine")
st.sidebar.image("descriptor.png")
st.sidebar.caption("Integration of sophisticated Vision Detection A.I. & Eye Tracking Studies")
st.sidebar.caption("Predicts which areas and objects, people are most likely to notice when they first glance at an image")
st.sidebar.caption("Captures pre-attentive processing, that occurs during the first few seconds of viewing ads")
st.sidebar.header("Objective")
st.sidebar.caption("Understanding the impact of the brand creative in OOH media Environment")
st.sidebar.subheader("Key Assessment Metrics")
st.sidebar.caption("-Area of Interest Analysis")
st.sidebar.caption("-Heatmap Analysis")
st.sidebar.caption("-Region Analysis")
st.sidebar.caption("-Gaze Sequence Analysis")
st.sidebar.caption("-Visual Elements Analysis")

#ACO Reports- Image Files

st.subheader("Creative Report Summary")
st.image("Reportsummary.jpg")
st.image("Locationsummary.jpg")


st.subheader("Deep Dive")

st.caption("1-Area of Interest Analysis")
image_comparison(
	img1="OOH-LED-97NguyễnThịMinhKhaiQ1TP-01_VAS_Original.jpg",
	img2="OOH-LED-97NguyễnThịMinhKhaiQ1TP-01_VAS_AreaOfInterest.jpg",
	label1="Original Creative",
	label2="Area of Interest Analysis",
)

st.caption("2-Heatmap Analysis")
image_comparison(
	img1="OOH-LED-97NguyễnThịMinhKhaiQ1TP-01_VAS_Original.jpg",
	img2="OOH-LED-97NguyễnThịMinhKhaiQ1TP-01_VAS_Heatmap.jpg",
	label1="Original Creative",
	label2="Heatmap Analysis",
)

st.caption("3-Region Analysis")
image_comparison(
	img1="OOH-LED-97NguyễnThịMinhKhaiQ1TP-01_VAS_Original.jpg",
	img2="OOH-LED-97NguyễnThịMinhKhaiQ1TP-01_VAS_Regions.jpg",
	label1="Original Creative",
	label2="Regions Analysis",
)

st.caption("4-Gaze Sequence Analysis")
image_comparison(
	img1="OOH-LED-97NguyễnThịMinhKhaiQ1TP-01_VAS_Original.jpg",
	img2="OOH-LED-97NguyễnThịMinhKhaiQ1TP-01_VAS_VisualSequence.jpg",
	label1="Original Creative",
	label2="Regions Analysis",
)

st.caption("5- Visual Elements Analysis")
st.image("OOH-LED-97NguyễnThịMinhKhaiQ1TP-01_VAS_VisualElements.jpg", width=None)
