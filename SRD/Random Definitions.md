# Random Definitions

## A Point Is On The Ground

A point $p$ is on the ground if $p$ lies on the surface of an object and $\vec{g} \cdot \vec{n} < 0$ where $\vec{g}$ is the direction of gravity, and $\vec{n}$ is the surface normal at $p$.

## An Area Is On The Ground

A continuous surface $S$ is on the ground if the entirety of $S$ lies on the surface of an object, and

$$
(\iint_{S} dS)^{-1} \cdot \iint_{S} \vec{g} \cdot \vec{n}_{x, y, z} \ dS < 0
$$

where $\vec{g}$ is the direction of gravity, and $\vec{n}$ is the surface normal at $(x, y, z)$ for $(x, y, z) \in S$.

Note that this definition is not completely strict. Minor discontinuities in the surface should be ignored. For example, if there is a crack in the ground that goes 200 meters deep, but is only a millimetre wide (for some reason), then a surface that crosses the crack should still be on the ground, ignoring the minor discontinuity of crossing the crack. It is also worth noting that nobody should ever have to compute this integral in real gameplay.
