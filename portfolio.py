import streamlit as st

# Title
st.title("My Developer Portfolio")

# Introduction
st.header("Introduction")
st.write(
    "Hello! I'm Priyadarshee, a full-stack developer with expertise in JavaScript, React, Node.js, and Java. "
    "I specialize in building scalable applications and APIs. Here's a showcase of some of my work."
)

# Skills Section
st.header("Skills")
st.write(
    "Some of the technologies and tools I work with include:"
)
skills = ["JavaScript", "React", "Node.js", "Java", "Spring Boot", "SQL", "Docker", "Kubernetes", "Firebase", "PostgreSQL"]
st.write(", ".join(skills))

# Projects Section
st.header("Projects")
st.write("Below are some of my notable projects:")

# Project 1: Railway Ticketing System
st.subheader("Project 1: Railway Ticketing System")
st.write(
    "A scalable and efficient railway ticketing system using gRPC-based microservices. Built with Spring Boot and Java, "
    "this system ensures improved performance and scalability."
)

# Project 2: URL Shortener
st.subheader("Project 2: URL Shortener")
st.write(
    "A URL shortening service that takes long URLs and converts them into shorter versions. Built using Node.js and deployed using Docker."
)

# Project 3: Student Fest Management System
st.subheader("Project 3: Student Fest Management System")
st.write(
    "A web-based system to manage events, participants, and schedules for a student fest. Built with React and Node.js."
)

# Contact Section
st.header("Contact")
st.write("Feel free to reach out to me for collaboration or job opportunities!")

# Social Media Links
st.markdown("[LinkedIn](https://www.linkedin.com/in/priyadarshee-kumar-32770a241/)")
st.markdown("[GitHub](https://github.com/Kp-Cyber3721)")
st.markdown("[Email] priyadarsheekumar18@gmail.com")
