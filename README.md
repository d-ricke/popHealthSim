# popHealthSim

The general idea of this project is to create a simulator to assist population health management, public healthcare policy, and perhaps even down to the community or hospital level.

We begin by modeling a person in person.py. We will keep this person as simple as possible in order to enable scaling this in world's as large as possible. The person will have some genetic inheritence from its parents, and some limited personality, habits, activities, perhaps other characterists that are mainly assigned randomly (perhaps based on location factors?). In addition, the person will keep a detailed medical history, both "real" in the sense of when the person actually gained the issue and "diagnosed" which records that which the person and doctors identify the issues. 

medicalIssue.py will model diseases, illnesses, injuries, or any other event or issue of medical significance that could affect a person. We will ideally eventually align to ICD-10 (or whatever number it is up to when we get there) but initially will begin with just a few related issues.

doctor.py will be a type of person who has extensive knoweldge of medicine and is qualified to make formal diagnoses of medical issues. Note that anyone can observe symptoms and gain beliefs of what their medical issues, but only doctors can make a formal diagnosis. Doctors can also prescribe medicine and treatments. 

I'm not sure at this moment what else to model, perhaps hospitals, schools, workplaces, shopping centers? activities? water treatment and distribution, food supply chains? 