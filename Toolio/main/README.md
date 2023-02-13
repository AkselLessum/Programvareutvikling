# PU 48

### HTML Structure
We utilize a base.html which contains the neccessary HTML information that all other HTML templates will inherid
This is mainly the base HTML info such as the <html> tags, as well as a navigation bar that references the other templates.
The createAd template shows the form needed to create an ad, filling this out will take you to the home template.
The home template displays ads

### Ads
In models.py we have the ad class, which is the class for all ad objects.
Ads can either be a normal ad, or a request ad. This is defined by the boolean variable isRequest.

The form in createAd.html sends a POST request, which will be interprereted by views.py and create a new ad object with the given information.