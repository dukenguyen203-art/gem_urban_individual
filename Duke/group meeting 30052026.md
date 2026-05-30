Data profiling



Transfers table

\-all rows has from\_stop\_id the same as to\_stop\_id

\-all transfer\_type is 4; 

(keep because tram and bus might have different values)

\- need a composite PK (from\_trip\_id, to\_trip\_id)

\- check code:

with check\_transfer\_PK as 

( select from\_trip\_id, to\_trip\_id

from gtfs\_metro\_train\_transfers gmtt 

group by from\_trip\_id, to\_trip\_id

having count(\*) >1

)

select count(\*) from check\_transfer\_PK





Stop\_times table

\- stop sequence only has 32 unique value -> cannot use as PK

\- recommend use composite PK (trip\_id, stop\_sequence)

\- check code: 

with stop\_times\_Pk\_duplicate as

(select trip\_id, stop\_sequence, count(\*) as No\_of\_duplicate

from gtfs\_metro\_train\_stop\_times

group by (trip\_id, stop\_sequence)

having count(\*) >1

)

select count(\*)

from stop\_times\_Pk\_duplicate





Shapes table

\- shape\_id only have 1748 unique value -> cannot use as a PK

\- recommend use composite PK (shape\_id, shape\_pt\_sequence)

\- check code:

with shapes\_Pk\_duplicate as

(select shape\_id, shape\_pt\_sequence, count(\*) as No\_of\_duplicate

from gtfs\_metro\_train\_shapes

group by (shape\_id, shape\_pt\_sequence)

having count(\*) >1

)

select count(\*)

from shapes\_Pk\_duplicate



Route tables:

\- data inconsistency: Werribee replacement bus

\- recommend creating a full\_name column, indicating replacement bus for each route



Calendar\_dates table

\- This table indicates service exceptions -> PK should be composite (date, service id) to adhere to the logical meaning and scalability





stops table:

\- parent\_station has no corresponding PK









Initial steps for silver



combine **routes** and **agencies** tables

combine **levels** and **stops** tables

split **shapes** table into:

&#x09;- **shapes**: shape\_id (PK), shape\_start\_lon, shape\_start\_lat, shape\_end\_lon, shape\_end\_lat, 	shape\_total\_distance

&#x09;- **shape\_details**: shape\_detail\_id (FK), shape\_id (PK), other columns

create surrogate primary key for composite keys in **stop\_times, calendar\_dates, transfers, shape\_details**

**calendar\_dates, transfers, shape\_details, pathways** tables should not be connected into the main data model

consider create a minor data model to futher analyse **stops, transfers, pathways**

consider filling all null **parent\_station** in **stops** table



