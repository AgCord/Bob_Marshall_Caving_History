# Bob Marshall Alpine Caving History Database

## Database description

This database records the public history of alpine caving in the Bob Marshall Wilderness Complex in Montana. The focus is notable people, named cave systems, expeditions, and the three published karst zones where that work has taken place: Silvertip, Scapegoat, and Turtle Mountain (Turtlehead).

The project is a working register of published facts, not a cave-location catalog and not a complete history. Location is stored only as a published zone name and county. No coordinates, trailheads, approach notes, or unpublished passages are included. The long-term aim is to support later writing about the people and expeditions that pioneered and continued this work. This first version meets the course minimum and includes a few extra published rows so all three zones are represented. The set will grow over the semester.

## Entities and sample instances

Each entity type has at least three descriptive attributes. Instances below are examples drawn from already-public sources.

### 1. Zone

A coarse, already-published alpine area inside the Bob Marshall / Scapegoat wilderness complex.

Attributes:

- name
- wilderness unit
- county (or counties)
- short public description

Sample instances:

- Silvertip: Bob Marshall Wilderness; Lewis and Clark / Flathead area as published; high alpine karst worked since the early 1970s, including the Silvertip Cave System.
- Scapegoat: Scapegoat Wilderness (Bob Marshall Wilderness Complex); Lewis and Clark / Powell Counties; alpine karst described in print in the 1970s, with a named cave system still being surveyed in later public expedition accounts.
- Turtle Mountain: Bob Marshall Wilderness; published as Turtlehead / Turtle Mountain; area associated with Tears of the Turtle and Virgil the Turtle’s Greathouse.

### 2. Person

A caver, surveyor, scientist, or expedition leader who appears in published accounts of this area.

Attributes:

- full name
- public role (pioneer, surveyor, expedition leader, scientist, etc.)
- active period (years or decade range)
- why they appear in the public record

Sample instances:

- Mike McEachern: pioneer / surveyor; 1970s onward; among the first to do sustained work on the Silvertip karst, later interviewed and exhibited as a Montana caving figure.
- Newell P. Campbell: scientist; 1970s; published NSS papers on Scapegoat and Bob Marshall alpine karst.
- Jason Ballensky: expedition leader / surveyor; 2000s onward; public record for discovery and later depth pushes at Tears of the Turtle and related Turtle Mountain caves.

### 3. Expedition

A dated, publicly reported trip or campaign that changed what was known about a zone or cave. 

Attributes:

- label
- year
- zone
- public outcome (one sentence)

Sample instances:

- 1973 Silvertip reconnaissance: 1973; Silvertip; early systematic work that opened sustained exploration of the Silvertip karst.
- 1973 Scapegoat alpine karst study: 1973; Scapegoat; Campbell’s published description of the Scapegoat plateau karst and related caves.
- 2014 Tears of the Turtle depth expedition: 2014; Turtle Mountain; published push that took the cave past Lechuguilla’s limestone-depth mark in the continental United States.

### 4. Cave

A named cave or system that already appears in public sources. Stored as a historical subject, not as a site to visit.

Attributes:

- published name
- zone
- year first documented in print (or first public discovery year as published)
- published length and/or depth when those figures are already public

Sample instances:

- Silvertip Cave System: Silvertip; public exploration record from the 1970s; published as a multi-mile alpine system (often discussed together with Blood Cave).
- Scapegoat Cave: Scapegoat; publicly described as known since the 1970s and still the subject of later published survey expeditions.
- Tears of the Turtle: Turtle Mountain; discovery publicly given as 2006; published depth and length have been updated in later news and reference sources.

## Questions / use cases

1. For a given zone, list the published expeditions in date order.
2. For a given cave, list the people and expeditions tied to its public discovery and later notable pushes.
3. List people whose published work falls in a chosen decade, and which zones they are tied to.

## What this first version does not include

- coordinates, GPS, maps, or travel directions
- unpublished caves, leads, or personal trip details
- private contact information
- a claim that the record is complete

Sources for later expansion include published NSS material, newspaper and magazine accounts, grotto talks already on the public web, and other print sources. Private interviews and member-only files are out of scope until permission exists.
