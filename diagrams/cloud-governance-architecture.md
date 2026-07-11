# Cloud Governance Platform Architecture

```text
                    Agentic Control Plane (ACP)
                               |
                               v
                Cloud Governance Platform
                               |
    ---------------------------------------------------------
    |                  |                 |                  |
    Compliance      Cost Agent     Security Agent    Resource Agent
       Agent                              |
           \              |               |              /
            \             |               |             /
             ------------- Governance Workflow ---------
                               |
                    -------------------------
                    |          |            |
               AWS Scanner  Policy Engine  Cost Analyzer
                               |
                               v
                     AWS Cloud Resources
