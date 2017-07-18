Matt Drury's Time Series Lecture
================================

This lecture is delivered from a Jupyter notebook.  Student interaction is provided by cells where students can write simple code to solve problems that come up in lecture, using functions provided earlier in the notebook.


Building
--------

Make sure that you have the development version of statsmodels installed for the seasonal ARIMA model used at the end of the lecture.  The following command should do:

```
pip install git+https://github.com/statsmodels/statsmodels.git
```

Objectives
----------

I used the following objectives for my lecture:

  - Define "time series" and "time series data".
  - Identify fundamental concepts in a time series: trend, seasonality, stickyness.
  - Use the classical decomposition to decompose and then describe a time series.
  - Define stationarity, contrast with independence.
  - Identify a stationary time series.
  - Fit ARIMA models to forecast a stationary time series.


Morning and Afternoon
---------------------

The morning lecture focuses on fundamental concepts and the classical decomposition.  The afternoon lecture focuses on stationarity and ARIMA models.  This break is in sync with the individual and pair excersizes.


Before the Lecture
------------------

The most confusing part of this lecture is MA models.  My approach here is to first introduce MA as *data generating processes* and then reverse the idea to ask

> Given some time series data you found in nature, what MA process is most likely to generate the data?

This is most effective if students already have some familiarity of the fundametal duality between probability and statistics:

  - **Probability** is the study of how we can design processes to generate data.
  - **Statistics** reverses the question, here we study, given some data, what process is *most likely* to generate data that looks like it.

Before starting the afternoon lecture, it would be a good idea to remind them of this idea, and possibly how it has applied to models we have studied up to that point.


Key Points for Student Interaction
----------------------------------

The notebook has cells that are built in to provide interaction with students.  These are labeled:

  - **Activity**: An oppurtunity for students to write some code using templates and functions provided earlier in the notebook.
  - **Question**: A simple question for students.  Ask, pause for a few moments, then call on a random student.
  - **Discussion**: A deeper, more conceptual question.  Have students discuss amongst themselves, then call on a willing student.  You will not have time to do all of these, so be selective of what you think is important.
