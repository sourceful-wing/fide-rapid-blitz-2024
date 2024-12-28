import { race } from "racing-bars";

/** @type {import('racing-bars').Options} */
const options = {
  autorun: true,
  makeCumulative: true,
  dateCounter: 'Round DD',
  fixedScale: true,
  tickDuration: 1000,
  showGroups: true,
  topN: 20,
  showIcons: true,
  title: "FIDE World Rapid Open 2024"

};

race("https://raw.githubusercontent.com/sourceful-wing/fide-rapid-blitz-2024/2893a1337db17bc8153cfba2f81667b03b9bace2/combined_players.json", "#race", options);
