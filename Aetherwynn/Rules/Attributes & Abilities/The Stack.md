## The Stack

The Stack is the most foundational concept in *Aetherwynn*. All abilities, triggers, and effects go through the stack when used. Once you understand the stack and its implications, you will understand *all* abilities in *Aetherwynn*.

### What Is A Stack?

Before we cover what the stack in *Aetherynn* is, it's best to discuss what a stack in general is. Put plainly, a stack can be imagined like a stack of paper. You put each sheet on top one at a time, and them remove each sheet starting from the top. For visualization's sake, see the figure below.

| Stack  |
| :----: |
| Item 3 |
| Item 2 |
| Item 1 |

Seeing this, your first thought might be: "Wait a second, aren't those number's backwards?" And you would be correct, if we were thinking about *removal order*. However, in this example, the items are numbered by *insertion order.* That's because when we insert an item into a stack, the latest item sits on the top, while older items are pushed below. So for the example above, the order of insertion goes:

$$
\textbf{Item 1} \to \textbf{Item 2} \to \textbf{Item 3}
$$

Now, for *removal* from the stack, it then follows that the order would be:

$$
\textbf{Item 3} \to \textbf{Item 2} \to \textbf{Item 1}
$$

Notice how the order of removal is the *reverse* of insertion order. This property is extremely helpful, as it allows us to easily do two things:
1. Remember *what* was put on the stack.
2. Encode the order that items will be removed.

Now for some vocabulary. Whenver we want to insert an item into a stack, we call that "pushing" the item "onto" the stack. And whenver we want to remove an item from a stack, we call that "popping" the item "off" the stack, or "popping" the item "from" the stack (either is fine). And like, that, we have concluded our little prelude.

### The Event Stack

*The Stack* is a gameplay abstraction first and foremost, meaning that all rules explained here have no bearing on in-world mechanics. They merely serve as a way of managing the events which will occur whever a player or the GM wishes to resolve an ability, deal daamge, etc.. This means that from this point and beyond, we will discuss the stack from purely a game-mechanical perspective.

Some terminology:
1. Ability — This refers to any activated/triggered ability which appears on an object/character sheet/monster stat block, etc.. Spells, Exploits, Class Abilities, all count as abilities.
2. Activated Ability — An ability that is not passive, and requires the controller of the entity which the ability belongs to to specifically activate it.
3. Triggered Ability — Usually a passive ability, it "triggers" whenever an event that is observed by that ability happens.
4. Event — An ability is used, or triggered, or any effect that would modify the game-state of an entity. The term acts as a general catch-all word for everything that goes on the stack.
5. Stack Frame — The state the stack is currently in (like a frame in a video or game).

**Pushing Events Onto The Stack.** Whenever an event occurs, that event is pushed onto the stack. Effects are never simultaneous, thus they are pushed onto the stack one at a time, until no more events can be pushed onto the stack.

Let's use the following interaction as an example:

> [!IMPORTANT]  
> *Alice attacks Bob. Bob casts "Shield". Claire uses "Bardic Inspiration" on Alice.*

Utilizing the stack structure we explored earlier, we can push each event onto the stack such that the stack looks like this (going from top to bottom):

| Stack                                    |
| :--------------------------------------- |
| Claire: "Bardic Inspiration" $\to$ Alice |
| Bob: "Shield"                            |
| Alice: Attack $\to$ Bob                  |

Here we are using an arrow to signify what each ability is targetting. As can be observed, the inciting incident (Alice attacking Bob) sits at the bottom of the stack, with each subsequent reaction sitting on top. Now we can cover...

**Popping Events Off The Stack.** Once our stack has been populated, we want to *resolve* the stack, which involves popping items from the stack, one by one, from top to bottom. It is important to note here, that items can be pushed onto the stack while the stack is resolving. This is because when resolving the stack, the item is popped off *before* any effects occur. This allows for any events occurring due to another effect resolving to be put onto the stack.

We will continue our example from above, resolving the stack step-by-step.

**Step 1:** Claire's "Bardic Inspiration" resolves. Current stack frame:

| Stack                   | Events in Resolution                     |
| :---------------------- | :--------------------------------------- |
| —                       | Claire: "Bardic Inspiration" $\to$ Alice |
| Bob: "Shield"           |                                          |
| Alice: Attack $\to$ Bob |                                          |

As we can see, Claire's ability has moved off the stack, and is ready to be resolved. Since no other abilities are being added to the stack at the moment, Claire's ability is free to resolve, which changes the stack frame so that it looks like this:

| Stack                   | Events in Resolution |
| :---------------------- | :------------------- |
| Bob: "Shield"           | —                    |
| Alice: Attack $\to$ Bob |                      |

**Step 2:** Notice how there are no events in resolution, this means that Bob's ability is now free to resolve. I will spare you the details, which leaves the new stack fram looking like this:

| Stack                   | Events in Resolution |
| :---------------------- | :------------------- |
| Alice: Attack $\to$ Bob | —                    |

**Step 3:** Alice now resolves her attack...

| Stack | Events in Resolution    |
| :---- | :---------------------- |
| —     | Alice: Attack $\to$ Bob |

However, now things get complicated. An attack in fact adds *multiple* events to the stack, each resolving conditionally depending on the previous step. But that's no matter, we can once again go step-by-step:

**Step 3.1:** The attack roll:

| Stack                          | Events in Resolution    |
| :----------------------------- | :---------------------- |
| Alice: *Attack Roll* $\to$ Bob | Alice: Attack $\to$ Bob |

**Step 3.2:** If the attack failed, the stack would be empty and nothing else would happen. But for the sake of example, lets say Alice's attack succeeds against Bob, thus the damage event is added to the stack.

| Stack             | Events in Resolution           |
| :---------------- | :----------------------------- |
| Alice damages Bob | Alice: *Attack Roll* $\to$ Bob |

At this step, Bob's party mate, Dennis realizes he has a reaction! He uses "Spiritual Ward" to protect Bob from Alice's attack, thus modifying the stack frame:

| Stack                              | Events in Resolution           |
| :--------------------------------- | :----------------------------- |
| Dennis: "Spiritual Ward" $\to$ Bob | Alice: *Attack Roll* $\to$ Bob |
| Alice damages Bob                  |                                |

**Step 4:** With no other reactions, we can continue resolving the stack, meaning the next stack frame is:

| Stack             | Events in Resolution               |
| :---------------- | :--------------------------------- |
| —                 | Dennis: "Spiritual Ward" $\to$ Bob |
| Alice damages Bob |                                    |

Thus Bob gains `3d8` *Temporary HP* **before** Alice's attack deals damage. Thus, when Alice's attack is finally allowed to resolve...

**Step 5:** The stack frame looks like this:

| Stack | Events in Resolution |
| :---- | :------------------- |
| —     | Alice damages Bob    |

Alice deals however much damage to Bob, who subtracts the amount from the *Temporary HP* granted by Dennis, and then any remaining damage is subtracted from his *HP*.

**Step 6:** With all events having completed, the stack is empty:

| Stack | Events in Resolution |
| :---- | :------------------- |
| —     | —                    |

Allowing gameplay to continue as normal, to Alice's next action, the next turn, etc. until a new stack of events occurs.
