# Meeting Notes Generator - Teams App

## Prerequisites
1. [Node.js](https://nodejs.org/) (LTS version)
2. [Teams Toolkit](https://marketplace.visualstudio.com/items?itemName=TeamsDevApp.ms-teams-vscode-extension)
3. [Visual Studio Code](https://code.visualstudio.com/)
4. A Microsoft 365 developer account (free)

## Setup Steps

1. **Register your app in Teams Developer Portal**
   - Go to [Teams Developer Portal](https://dev.teams.microsoft.com/)
   - Sign in with your Microsoft 365 account
   - Click "New app"
   - Fill in the app details
   - Save the generated App ID

2. **Update the manifest**
   - Replace `{{TEAMS_APP_ID}}` in `manifest.json` with your App ID
   - Update the URLs in the manifest with your actual deployment URLs
   - Create and add app icons (192x192 pixels)

3. **Create app icons**
   - Create two PNG files:
     - `color.png`: Full color icon
     - `outline.png`: Outline version of the icon
   - Place them in the `teams` directory

4. **Package the app**
   ```bash
   npm install -g teamsfx-cli
   teamsfx package
   ```

5. **Test the app**
   - Upload the generated package to Teams
   - Test in Teams client

## Deployment

1. **Deploy the backend**
   - Deploy to Azure App Service or similar
   - Note the backend URL

2. **Deploy the frontend**
   - Deploy to Azure Static Web Apps or similar
   - Note the frontend URL

3. **Update URLs**
   - Update all URLs in the manifest
   - Update the frontend's environment variables

4. **Submit to Teams App Store**
   - Package the app
   - Submit for review
   - Wait for approval

## Development

To test locally:
1. Start the backend server
2. Start the frontend server
3. Use Teams Toolkit to sideload the app
4. Test in Teams client

## Troubleshooting

Common issues:
1. App not loading: Check CORS settings
2. Authentication errors: Verify app permissions
3. Icon issues: Ensure correct size and format 