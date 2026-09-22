import streamlit as st 

st.title("GYM SET & REP TRACKER")


exercise = st.text_input("What exercise are you doing?: ")


sets, target_reps = st.columns(2)

with sets:
    sets = st.number_input("How many sets are you doing?: ", min_value=0, step=1)
    if sets <= 0: 
        st.warning("Invalid Entry")
        st.stop()
    else: 
        st.success(f"Great! Lets get to work. We are locking in for {sets} sets of {exercise}")

with target_reps:
    target_reps = st.number_input("What is your target rep for this specific workout: ", min_value=0, step=1)
    if target_reps <= 0:
        st.warning("Invalid Entry!")
        st.stop()
    else:
        st.success(f"You're a beast! Lets get it! Hitting {target_reps} reps on each set today.")


rep_count = 0

st.write("\n")

for set in range(1, int(sets) + 1):
    reps = st.number_input(f"How many reps did you do on set {set}?: ", key=f"set_{set}", min_value=0, step=1)
    rep_count += reps
st.write("\n")    

st.success(f"You did {sets} sets and {rep_count} total reps of {exercise} ")


target_reps = target_reps * sets

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Total Reps Completed", value=rep_count)
    
with col2:
    st.metric(label="Target Rep Goal", value=target_reps)



completion = rep_count / target_reps
st.progress(min(completion, 1.0))



if rep_count >= 30:
    st.success("DAMN! Save some reps for us bro haha. You were flying in there")
else:
    st.write("Dont Worry man, we focus and lock in next sesh")
    
if rep_count < target_reps * sets:
    st.write("Not hitting your target reps today is fine. Better to keep good form than to do random movements :)")
else:
    st.success(f"AMAZING! You hit your target amount of reps. Pushing through {target_reps * sets} reps on {sets} different sets is crazy. Insane bruv!")
    
    