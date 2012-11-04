# MATHer Blather

As I go through reviewing the maths from Khan Academy I will be attempting to put convert those concepts into code,
and that code will live in this repository.  While there are currently no plans for what to do with this collection
of scripts I believe it may become the basis of a library for a simple CLI calculator app.

## Caveats
### Prime Factorization

Prime numbers are stored in a hard coded list that only goes up to 997.  The decision to stop there was arbitrary
and the list can be expanded if need be.

## Future Ideas
### Prime Number Generator

Generate and store the list of primes locally on the user's machine for a more individual balance of performance
vs. range.

### Caching

Cache the output of any calculation where the cost to calculate is greater than the cost to look it up from cache.
Could make this a pretty highly performant library for doing the maths.