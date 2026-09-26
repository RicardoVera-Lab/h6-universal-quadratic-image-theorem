# H6 in Plain Language

Imagine a machine with **6 binary switches**. It can be placed in 64 different input states.

The machine produces **12 binary lights** as output. Its programming is restricted: every output light may use only a Boolean rule of algebraic degree at most 2.

Now choose any 24 different output patterns you want.

The theorem says:

> **There is always some legal quadratic programming of the machine whose 64 possible outputs include all 24 patterns you selected.**

The surprising part is the number 24.

The scalar quadratic function space has dimension only 22. If the input locations were fixed beforehand, 22 would be the natural arbitrary-interpolation limit.

H6 succeeds at 24 because the input points are chosen *after* seeing the targets.

With 24 evaluation points living in a 22-dimensional evaluation space, two dependency relations are unavoidable.

But 24 target vectors living in 12 dimensions already have at least 12 relations.

H6 shows that the selected preimages can be arranged so that the two unavoidable relations on the input side are relations the target data already satisfy.

In simple terms:

> **We did not make the box bigger. We learned how to place the two unavoidable constraints where they do not hurt.**

That is the mechanism behind the 22-to-24 gain.

The next scientific question is whether the same dependency-matching idea works systematically in larger dimensions. That is a separate research program and is not assumed by this theorem.
