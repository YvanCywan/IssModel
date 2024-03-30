# Iss Modelling

## Preface

In 2021, I started to work on a University Group Project that involved modelling the manoeuvring of the ISS to dodge debris through the use of a control moment gyroscope (CMG).

I recently reviewed the paper my group wrote on the computational mode and noticed the glaring inaccuracies in the results (to be fair, we noticed them then). This has given me the idea to do a reboot of the project, attempting to get a closer report.

There were a lot of things we ignored during that project, from a programming perspective, these include: 
1. Object-Oriented Programming (OOP)
2. Test Driven Development (TDD)
3. Behaviour Driven Development (BDD)
4. CI

These are things that we ignored then, but I think they are important to consider now. We ignored them due to time constraints, and looking back I believe that was the wrong decision. The reason for that, is that these practises allow us to spend more time worrying about the design of the model, rather than how we actually worry about the implementation.