# -*- coding: utf-8 -*-
"""graphs25

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j04VPqQ1Y2zeauM5YdyzEb8JnMlW6LB-
"""

import streamlit as st
import pandas as pd
import plotly.express as px


#title of the app
# Add an image to the top left corner of the sidebar
st.image("photos/Daily rounds logo.jpeg", width=100)  # Adjust the width as needed

st.title('Top Consumption Analysis and YOA Analysis - Insights')
# Add a header image
header_image = "photos/bannermarrow.png"  # Replace with the path to your header image
st.image(header_image, use_column_width=True)
# Add text to the Streamlit app
st.markdown("""
### YOA Analysis

In YOA analysis, the observations are as follows:

- The maximum usage comes from Doctors who are not students currently. First year student however are found to have video usage on almost all popular subjects like OBG, ENT, etc. and an ample about of QBanks.
""")


# Sample data
year = ['First Year', 'Second Year', 'Third Year', 'Fourth Year', 'Final Year', 'Internship', 'Doctor']
video_counts = [1129, 1299, 1709, 1714, 2489, 1692, 2956]

# Create a dictionary to store the data
data = {'YOA': year, 'Video Count': video_counts}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Sort the DataFrame by the 'Month' column
df_sorted = df.sort_values(by='YOA')

# Plot a bar chart
fig = px.line(df_sorted, x='YOA', y='Video Count', title='Distinct Count of Video Titles by YOA')
st.plotly_chart(fig)

# List of subject titles
subject_titles = ['Dermatology', 'Psychiatry', 'Microbiology', 'Biochemistry']

# Dictionary mapping subjects to average completion time
average_completion_time = {
    'Dermatology': 30,
    'Psychiatry': 25,
    'Microbiology': 35,
    'Biochemistry': 40
}

# Create a dropdown menu
selected_subject = st.selectbox('Select a Subject To Check For Average Pace of Completion', subject_titles)

# Display the selected subject
st.write('You selected:', selected_subject)

# Display the corresponding average completion time
if selected_subject in average_completion_time:
    st.write('Average Completion Time In Days:', average_completion_time[selected_subject])
    st.markdown(f"<p style='font-size: 24px;'>{average_completion_time[selected_subject]}</p>", unsafe_allow_html=True)
else:
    st.write('Average Completion Time: N/A')

# Add text to the left sidebar

st.sidebar.header('💡Insights At A Glance')

st.sidebar.markdown("""
    Majority users have a spike starting from April, and Aug - November highest usage
    Most of them are doctors
    Heavy usage in the second half of the year
    Extreme consistency maintained
""")

import streamlit as st
import pandas as pd
import plotly.express as px

# Updated sample data to include specific times for First Year
data = {
    'Academic Year': ['First Year', 'Second Year', 'Third Year', 'Fourth Year', 'Final Year', 'Internship', 'Doctor'],
    'Morning Study Start Time': [6, 7, 6, 11, 8, 9, 11],  # Assuming placeholders for other years
    'Morning Study End Time': [9, 11, 9, 12, 11, 11, 3],  # Assuming placeholders for other years
    'Evening Study Start Time': [18, 8, 19, 19, 18, 17, 16],  # Assuming placeholders for other years
    'Evening Study End Time': [22, 23, 23, 24, 23, 24, 19],  # Assuming placeholders for other years
}

# Create a DataFrame
df = pd.DataFrame(data)

# Content for Academic Years tab
st.title('Academic Years')
selected_year = st.radio('Select Academic Year', df['Academic Year'])

# Filter data based on selected academic year
selected_row = df[df['Academic Year'] == selected_year].reset_index()

# Prepare data for plotting
plot_data = pd.DataFrame({
    'Event': ['Morning Study Start', 'Morning Study End', 'Evening Study Start', 'Evening Study End'],
    'Hour': [
        selected_row.loc[0, 'Morning Study Start Time'],
        selected_row.loc[0, 'Morning Study End Time'],
        selected_row.loc[0, 'Evening Study Start Time'],
        selected_row.loc[0, 'Evening Study End Time']
    ]
})

# Plotting
fig = px.line(plot_data, x='Hour', y='Event', title=f'Study Times for {selected_year}',
              markers=True)

# Show plot
st.plotly_chart(fig)

# Updated sample data to include specific times for First Year
data5 = {
    'Academic Year': ['First Year', 'Second Year', 'Third Year', 'Fourth Year', 'Final Year', 'Internship', 'Doctor'],
    'Anatomy': [16, 17, 6, 11, 348, 9, 151],  # Assuming placeholders for other years
    'Biochemistry': [19, 11, 9, 212, 141, 121, 353],  # Assuming placeholders for other years
    'OBG': [18, 8, 19, 19, 158, 127, 169],  # Assuming placeholders for other years
    'ENT': [22, 12, 23, 24, 213, 244, 519],  # Assuming placeholders for other years
    'Medicine': [15, 17, 23, 24, 123, 624, 419],  # Assuming placeholders for other years
    'Surgery': [12, 23, 23, 24, 243, 724, 419],  # Assuming placeholders for other years
    'E6.5 Revision Videos': [2, 23, 23, 24, 623, 264, 169],  # Assuming placeholders for other years
}

#subject distribution year-wise

# Create a DataFrame
df5 = pd.DataFrame(data5)

# Content for Academic Years tab
st.title('Academic Years')

# Create a dropdown menu to select academic year
selected_year = st.selectbox('Select Academic Year', df5['Academic Year'])

# Filter data based on selected academic year
selected_row = df5[df5['Academic Year'] == selected_year].reset_index()

# Prepare data for plotting
plot_data = pd.DataFrame({
    'Event': ['Anatomy', 'Biochemistry', 'OBG', 'ENT', 'Medicine', 'Surgery', 'E6.5 Revision Videos'],
    'Hour': [
        selected_row.loc[0, 'Anatomy'],
        selected_row.loc[0, 'Biochemistry'],
        selected_row.loc[0, 'OBG'],
        selected_row.loc[0, 'ENT'],
        selected_row.loc[0, 'Medicine'],
        selected_row.loc[0, 'Surgery'],
        selected_row.loc[0, 'E6.5 Revision Videos'],
    ]
})

# Plotting
fig = px.bar(plot_data, x='Hour', y='Event', title=f'Study Times for {selected_year}')

# Show plot
st.plotly_chart(fig)


import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
video_counts = [422, 583, 634, 878, 976, 1032, 1365, 2321, 976, 834, 678, 476]

# Create a dictionary to store the data
data = {'Month': months, 'Video Count': video_counts}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Sort the DataFrame by the 'Month' column
df_sorted = df.sort_values(by='Month')

# Plot a bar chart
fig = px.bar(df_sorted, x='Month', y='Video Count', title='Distinct Count of Video Titles by Month')
st.plotly_chart(fig)



import streamlit as st
import matplotlib.pyplot as plt
import streamlit as st

# Add text to the sidebar
st.sidebar.markdown("""
<div style="display: flex; flex-wrap: wrap;">
  <div style="width: 103.33%; padding: 10px;">
      <p>Majority users have a spike starting from April, and Aug - November highest usage</p>
      <p>💡Most of them are doctors</p>
      <p>💡Heavy usage in the second half of the year</p>
      <p>💡Extreme consistency maintained</p>
      <p>💡45% out of 120 users have appeared in our top consumption list and further marked for an OTP_NV, but are not extremely suspicious. </p>
    </div>
  </div>
  <div style="width: 103.33%; padding: 10px;">
      <p>- The students usually study from tier 1 colleges</p>
      <p>- First years - 6am - 9 am and 2pm to 6 pm</p>
      <p>- Second years usually study from 7 am to 9 am and then 9 pm - 11 pm at night</p>
      <p>- Third years are found to have a similar pattern but the usage is more during late evening to night time.</p>
      <p>- The study session is for an average of 5 hours per day for most number of users</p>
    </div>
  </div>
  <div style="width: 103.33%; padding: 10px;">
      <p>- When we talk about the engagement on other content on the app, the ratio for video watch and qbanks is 1:4. That is, for every 4 videos watched, 1 qbank is solved.</p>
      <p>- The time gap between creating an account and buying the plan is 1 year constant throughout majority users.</p>
      <p>- Higher videos does not always mean high qbank usage and notes usage.</p>
      <p>- Subjects which are highly watched are OBG, Medicine, ENT and E6.5 Revision Videos have a spike after July.</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)



import matplotlib.pyplot as plt

# Sample data
labels = ['QBank Usage', 'Notes', 'Video Usage', 'Others']
sizes = [14, 34, 42, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create a pie chart with a smaller size
fig1, ax1 = plt.subplots(figsize=(4, 4))
ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# Set the font size of the legend
ax1.legend(labels, loc="center right", fontsize=3)
# Display the pie chart on the left side of the Streamlit app
st.pyplot(fig1)

# Add text to the right side of the Streamlit app
st.markdown("""
<div style="float: right; width: 50%;">
  <p>The following statistics has been obtained by taking the average of the count of each unique event present in the API logs for each user. An average of all the user's data has been displayed here.</p>
</div>
""", unsafe_allow_html=True)


import pandas as pd

# Sample data
data4 = {
    'Subject Name': ['Anaesthesia', 'Anatomy', 'Biochemistry', 'Cardiology', 'Community Medicine', 'COVID-19 Updates', 'Delta MCQ Discussion', 'Delta Recent Updates', 'Delta: MCQ Discussion videos', 'Dermatology', 'E6 MCQ Discussion', 'E6 Revision Videos', 'E6.5 Revision Videos', 'Endocrinology', 'ENT', 'Forensic Medicine', 'Gastroenterology', 'Gastrointestinal System', 'Haematology', 'Integrated Sessions', 'Marrow Live +', 'Marrow Revision Videos', 'Medicine', 'Microbiology', 'Nephrology', 'Neurology', 'Obstetrics & Gynaecology', 'Ophthalmology', 'Orthopaedics', 'Paediatrics', 'Pathology', 'Pharmacology', 'Physiology', 'Psychiatry', 'Pulmonology', 'Radiology', 'Rheumatology & Immunology', 'Surgery'],
    'Average Time Taken to Finish the Subject': [21.5, 71.1, 45.9, 16.2, 78.6, 5, 19, 7.6, 8.6, 22.7, 20.8, 32.3, 65.5, 14.8, 46.8, 27.0, 10.75, 1, 13.5, 2, 1, 27.6, 166.9, 57.7, 15.5, 8, 79.5, 29.4, 20.8, 42.0, 56.1, 56.2, 45.2, 13.48, 14.5, 29.9375, 9.875, 58.0]
}

# Create a DataFrame
df4 = pd.DataFrame(data4)

# Display the title as a markdown string
st.markdown("### Average time taken by a student to finish a subject from a pool of high consumption users")

# Display the DataFrame as a table
st.table(df4)


# Display the title as a markdown string
st.markdown("### Questions Under Hypothesis Answered Below")

import streamlit as st

# Create an expander for Question 1
with st.expander("Question 1: Is there a significant difference between the top completion users and normal users"):
    st.markdown("""
    Answer: There is a significant difference between a normal user and a top consumer. A normal user will complete the subjects without a pattern, but a top consumer finishes the subjects in a stretch. (refer to the table for avg days a subject takes to finish). Find the graph below.
    """)

import streamlit as st

# Create an expander for Question 2
with st.expander("Question 2: Majority of the top completion users are not from the same college"):
    st.markdown("""
    **Answer:** Most of the users belong to tier 1 medical colleges and also government medical colleges. Here is a list of top colleges:

    - Karnataka Institute of Medical Sciences, Hubballi
    - All India Institute of Medical Sciences, Bhubaneswar
    - Armed Forces Medical College, Pune
    - Assam Medial College, Dibrugarh
    - Belagavi Institute of Medical Sciences, Belagavi
    - Bukovinian State Medical University
    - Chamrajanagar Institute of Medical Sciences, Karnataka
    - Dr. Rajendar Prasad Government Medical College, Tanda, H.P
    - Government Dharmapuri Medical College, Dharmapuri
    - Government Medical College, Kota
    - Government Medical College, Kozhikode, Calicut
    - Government Thiruvannamalai Medical College, Thiruvannamalai
    - K A P Viswanathan Government Medical College, Trichy
    - Mahatma Gandhi Medical College & Research Institute
    - Nilratan Sircar Medical College, Kolkata
    - Seth GS Medical College, Mumbai
    - T S Misra Medical College & Hospital, Amusi, Lucknow
    """, unsafe_allow_html=True)

# Create an expander for Question 3
with st.expander("Question 3: Do top completion users did not finish the subjects in sequence?"):
    st.markdown("""
    Answer: Top consumption users finish the subject in a sequence and in a span of 2-3 months.
    """)




import streamlit as st

# Add text to the Streamlit app
st.markdown("""
### Conclusion

Based on the analysis of the study patterns of the students, several key insights can be drawn:

1. **Year of Admission (YOA) Analysis**: The data shows that students in their final year and during their internship phase tend to consume the highest number of video titles. This could be attributed to the increased focus on exam preparation and clinical exposure during these phases.

2. **Subject-wise Analysis**: The data indicates that certain subjects, such as Dermatology and Psychiatry, are more popular among students, as evidenced by the higher number of video titles consumed in these subjects.

3. **Time of Year Analysis**: There is a noticeable spike in video consumption during the months of April and August to November. This could be due to the timing of exams or the availability of new study materials during these periods.

4. **User Demographics**: The majority of users are doctors, which suggests that the platform is popular among medical professionals seeking to enhance their knowledge and skills.

5. **Study Duration**: The average time taken to complete a subject varies widely, ranging from a few days to several months. This could be due to differences in the complexity of the subject matter or the individual study habits of the students.

6. **Usage Patterns**: The data suggests that students tend to consume videos and solve QBank questions in a ratio of 1:4, indicating a preference for video-based learning followed by practice questions.

7. **Consistency**: Despite variations in study duration and subject popularity, there is a consistent pattern of usage among students, with heavy usage in the second half of the year and a consistent daily study duration of around 5 hours.

In conclusion, the study pattern analysis of the students reveals a consistent trend of heavy usage during specific periods of the year, a preference for certain subjects, and a balanced approach to learning through videos and QBanks.
""")
