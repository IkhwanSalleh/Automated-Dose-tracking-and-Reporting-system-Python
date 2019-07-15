# Automated-Dose-tracking-and-Reporting-system-Python
This is an Automated dose tracking and reporting system using Optical character recognition methods.
The objective of this algorithm is :

Problem: DICOM is a standard in Medical imaging its is used to make transfer of information and saving information easier.
         For example a CT scan perform on a CT scanner model A can be read on CT scanner model B without problem because they have the
         same format of DICOM format.
         
         Each year the number of CT scan performed around the world is increasing drastically. There is an increasing risk with increasing 
         use of CT scan since CT scanner using a higher radiation dose compared to the nomrmal convectional x-rays. As a method to know 
         the current practice we want to know what is called as diagnotic reference level in medical imaging. We want to know the current 
         radiation dose level comes from a CT scanner. If high radiation dose practice is given without strong justification the practice need
         to be reviewed again. To know the current dose level from CT we need to monitories the radiation dose by monitoring dose from CT dose
         screen inside a DICOM files. There are actually a new advanced where CT dose information is located inside the DICOM files but not in
         the CT dose screnn image type but not all CT scanner have that ability. The number of CT scan is increasing thus using computer the 
         task can be completed more efficiently instead of manually viewing the CT dose screen.
         
         Thus this, algorithm is used to automatically perform the task for us using the Optical character recognition method to read and archive
         T dose screen inforamtion into a structured database.
         
         the OCR engines is the brain of the algorithm used is the TesseractOCR . The algorithm is trained using 1000 sample of CT dose screen.
         The algorithm work perfectly with both number and word

Thank you for reading

Have a nice days
         
 
