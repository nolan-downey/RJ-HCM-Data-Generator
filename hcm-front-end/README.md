## HCM Data Generator Front End README

#### Structure

This app is written using ReactJS and the `create-react-app` tool. Prior to development,
(1) ensure you have the latest version of NodeJS installed and (2) make sure to run `npm i` 
in the root directory of the project.

`public
This contains all of the public resources for the app. Add logos and favicons as seen fit.

`src`
This contains all of the core functionality of the app in the form of React components and 
their stylesheets. Currently, all CSS is contained in `App.css`.
Put all additional functions and components into this folder.

#### Components
To add new components, simply refer to the ReactJS documentation. All components in this 
project are functional components rather than class components,
so it's best advised to keep following this style.

`App.js`
This is the app's main entry point after `index.js`. Instead of implementing routing, this project
uses the `useState` hook to keep track of which page the user is on. 
To add new views, you can either implement routing with a library like `react-router` 
or add additional frames via conditional rendering like so: `{frame === N && <FrameN />}`
passing props to FrameN as seen fit.

`frame0.js`, `frame1.js`, `frame2.js`
All of these are the various screens that will be displayed in the app. Add more frames as deemed necessary.

`nav.js`
This is the navbar heading the front end application. Feel free to add functionality to the navbar
as deemed necessary.

`literals.js`
This contains any magic strings or other literals that come handy in other files such as the 
API url.

`Loader.js`
This is the spinning wheel that displays when a query is running. Reuse this for any similar case.

#### To Start Development
To start development, simply clone this repository and run `npm i` in its root directory.
Run `npm start` to view the project at `localhost:3000`. To build the project
for deployment to Heroku, simply run `npm run build` and a `build` folder will appear
containing the assembled and minified app.