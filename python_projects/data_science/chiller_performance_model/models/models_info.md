| Model          | Description                                                | Validation Error | Manual Estimations Difference | Old Chiller Error |
|----------------|------------------------------------------------------------|------------------|-------------------------------|------------------|
| XGB_1.pkl      | XGB model, first model trained on whole 15-mins data 0-1.0 cload | 9.0%             | 57%                           | -                |
| XGB_2.pkl      | XGB model, trained on 15-mins data 0.3-1.0 cload           | 7.5%             | 35%                           | 9.6%             |
| XGB_3.pkl      | Same as XGB_2 but without leakage                          | 7.41%            | -                             | -                |
| XGB_4.pkl      | Same as XGB_3 but using the optimized temperature          | 7.63%            | 36%                           | 10.8%            |
| XGB_a1.pkl     | Uses optimized temperature, with an aggregation window of ±1 hours | 6.8%             | 38%                           | 9.5%             |
| XGB_a2.pkl     | Same as XGB_a1 but with ±2 hours                           | 6.6%             | 39%                           | 9.5%             |
| XGB_hr.pkl     | Uses weather.com hourly temperature                        | 8.9%             | 35%                           | 10.8%            |
| XGB_hr_a1.pkl  | Uses weather.com hourly temperature, with an aggregation window of ±1 hours | 8.1%             | 35%                           | 10.8%            |
| XGB_m_1.pkl    | Uses weather.com hourly temperature + aggregation window   | 8.4%             | 31%                           | 8.6%             |
| RFR_m_1.pkl    | Uses weather.com hourly temperature + aggregation window   | 6.7%             | 33%                           | 10.4%            |
| XGB_m_2.pkl    | Uses weather.com hourly temperature                        | 6.9%             | 28%                           | 8.6%             |
| RFR_m_2.pkl    | Uses weather.com hourly temperature                        | 6.6%             | 34%                           | 10.4%            |
