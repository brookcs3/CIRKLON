# Cirklon Hitbox Mapping Guide

## Overview
This guide will help you create precise hitbox coordinates for all controls on the Cirklon interface, using the Arturia-style photorealistic approach.

## Setup
1. Open `/Users/cameronbrooks/_CB/AI Library/CIRKLON/hitbox-mapper.html` in your browser
2. You'll see two background options:
   - **Cirklokn.svg** - Your detailed SVG reference
   - **1.svg** - Alternative background

## Mapping Process

### Step 1: Step Sequencer Buttons (1-16)
These are the main step buttons at the bottom of the unit.

**Instructions:**
1. Switch to the appropriate background image
2. Click and drag to create a hitbox over **Step Button 1** (leftmost button)
3. Note the coordinates that appear in the output
4. Repeat for buttons 2-16, moving left to right

**Expected Results:**
```
Step Button 1: x=?, y=?, width=?, height=?
Step Button 2: x=?, y=?, width=?, height=?
...
Step Button 16: x=?, y=?, width=?, height=?
```

### Step 2: Step Encoders (1-16)
The rotary encoders above each step button.

**Instructions:**
1. Create hitboxes over each encoder knob above the step buttons
2. Make sure to include the entire rotatable area
3. Record coordinates for each encoder 1-16

### Step 3: Transport Controls
Map the transport buttons (typically bottom left area):

- **Play Button** (▶)
- **Stop Button** (■)  
- **Record Button** (●)

### Step 4: Function Buttons
Map all labeled function buttons around the interface:

**Left Side:**
- SHIFT
- FILL  
- SOLO
- NEXT

**Right Side:**
- SAVE
- LAST
- SCULPT
- MENU
- COPY
- DELETE
- INSERT
- GANG

### Step 5: Main Encoders
Map the larger control knobs:

- **Row Encoder** (left side)
- **Bar Encoder** (right side)
- **Value Encoder** (near display)
- **Assignable Knobs A & B** (top right)

### Step 6: Display Area
Create a hitbox for the LCD display area (center of unit).

## Recording Format
For each control, record in this format:

```markdown
### [Control Name]
- **Type**: button/encoder/display
- **Background**: Cirklokn.svg or 1.svg
- **Position**: x=[left], y=[top]
- **Size**: width=[width], height=[height]
- **CSS**: `left:[left]px; top:[top]px; width:[width]px; height:[height]px;`
- **Function**: [what this control does]
```

## Quality Check
- Hitboxes should be slightly larger than visual elements for easier interaction
- No overlapping hitboxes
- Test that all areas are reachable
- Verify coordinates work on different screen sizes

## Next Steps
Once you have all coordinates mapped:
1. Export the JSON data using the "Export Coordinates" button
2. We'll create the interactive Cirklon component using these exact positions
3. Add visual feedback and audio connectivity

## Example Entry
```markdown
### Step Button 1
- **Type**: button
- **Background**: Cirklokn.svg
- **Position**: x=85, y=245
- **Size**: width=28, height=18
- **CSS**: `left:85px; top:245px; width:28px; height:18px;`
- **Function**: Triggers step 1 in the sequence
```

Start with Step Button 1 and work your way through systematically. Reply with your findings for each control as you map them!