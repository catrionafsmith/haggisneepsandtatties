### Haggis Neeps and Tatties - Automatic Recipe Suggestions
A Flask app which uses an external API to generate recipe suggestions.
v1 and v2 functionality is demonstrated below:

<p align="center"><img width="360" alt="recipe generator v1" src="https://user-images.githubusercontent.com/113362369/209400204-c8f7b44b-b66c-4882-817c-6198d6c1b241.gif">
<img width="360" alt="recipe generator v2" src="https://user-images.githubusercontent.com/113362369/209409781-2d702898-fa06-4b45-910c-538edf772fd2.gif"></p>

My parents always have trouble picking what to make for dinner, so I thought that I would try to make them something that would help them to decide on a recipe! (The name of this app is 'Haggis Neeps and Tatties', which is a traditional Scottish dinner.)

Built with: Flask was used to generate the site. TheMealDB.com external API was used to obtain recipe suggestions, images and links. I also added an external CSS stylesheet.

Contribution or Remixing Haggis Neeps and Tatties: Feel free to contribute or remix! To contribute, please do the following:

git clone this repo Go to the root folder of this project and checkout to another branch `git checkout {your-nickname}-rename-title Do your stuff git add . git commit -m "any descriptive message" git push origin {your-nickname}-rename-title Submit a PR for review

What I have learned: This was the first time that I had used Flask to create a website. I learned how to integrate output from an external API into my webpages through Flask. 

Issues I faced and how I resolved them: I wanted to add an external CSS file to my project, but I didn't realise that Flask needs all static files (like CSS) to be inside a folder labelled 'static'. Initially I was not sure how pages were rendered using Flask, but watching a video from another source clarified this.

Source: The recipes used in this app are obtained from TheMealDB.com under a free licence. The README.md template is by skirianov.

c2022
