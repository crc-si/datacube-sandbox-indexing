# Sandbox Indexing

A repository that holds scripts for indexing data in the FrontierSI sandbox.

This is a work in progress.

## Testing
To test, you can use a local Docker environment, and launch with the following steps:
 * Start the system with `make up` or `docker-compose up`
 * Initialise the ODC database with `make init`
 * Add products (currently only Sentinel) with `make add-products`
 * Run indexing with `make index-sentinel`
