# Random Definitions

## A Point Is On The Ground

A point $p$ is on the ground if $p$ lies on the surface of an object and $\vec{g} \cdot \vec{\mathbf{n}} < 0$ where $\vec{g}$ is the direction of gravity, and $\vec{\mathbf{n}}$ is the surface normal at $p$.

## An Area Is On The Ground

A continuous surface $S$ is on the ground if the entirety of $S$ lies on the surface of an object, and

$$
(\iint_{S} \mathbf{d}S)^{-1} \cdot \iint_{S} \vec{g} \cdot \vec{\mathbf{n}}_{x, y, z} \ \mathbf{d}S < 0
$$

where $\vec{g}$ is the direction of gravity, and $\vec{\mathbf{n}}$ is the surface normal at $(x, y, z)$ for $(x, y, z) \in S$.

Note that this definition is not completely strict. Minor discontinuities in the surface should be ignored. For example, if there is a crack in the ground that goes 200 meters deep, but is only a millimetre wide (for some reason), then a surface that crosses the crack should still be on the ground, ignoring the minor discontinuity of crossing the crack. It is also worth noting that nobody should ever have to compute this integral in real gameplay.

## A Point Is In Range

A point $\vec{p}$ ($\vec{p}$ is a vector representing a point) is in range of an ability if $\mathbf{distance}(\vec{p}, \vec{x}) \leq r$, where , $\vec{x}$ is the position of the creature using the ability, and $r$ is the range of the ability.

## A Creature Is In Range

A creature is in range of an ability if, on average, the creature is within range. This can be checked as follows.

$$
(\iiint_C \mathbf{d}C)^{-1} \cdot \iiint_C \mathbf{distance}(\langle x, y, z\rangle, \vec{x}) \ \mathbf{d}C \leq r
$$

Where $C$ is the smallest possible volume representing the targetted creature, $\vec{x}$ is the position of the creature using the ability, and $r$ is the range of the ability.

This roughly equates to half or more of the creature's volume being in range of the ability.

## A Point Is Inside An Area of Effect

A point $p$ is inside an Area of Effect $A$ if $p \in A$, where $p \in \mathbb{R}^3$ and $A \subset \mathbb{R}^3$.

Higher-dimensional gameplay is not yet supported.

## A Creature Is Inside An Area of Effect

A creature is inside and Area of Effect if at least half of the creature is inside the Area of Effect.

This can be expressed as

$$
\iiint_{A \cap C} \mathbf{d}(A \cap C) \geq \frac{1}{2}\iiint_{C} \mathbf{d}C
$$

where $A$ is the volume bounded by the Area of Effect, $C$ is the smallest possible volume representing the targetted creature, and $A \cap C$ is the intersection of those two regions.

This simply finds if the region of interection between the Area of Effect and the creature is half or more of the creature's volume.
