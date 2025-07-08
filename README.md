# LimitOrderBook-Sim 🏛️

Ultra-lightweight Python engine that **simulates an exchange-style limit order book** at ~1 M msgs/s on a single core.

## Key features
- Event-driven matching engine (price-time priority)  
- Supports market, limit, cancel, modify orders  
- Built-in latency + queue-position stats  
- CSV→Parquet logger for post-trade analysis

 # Limit Order Book Modeling Project (July 2025)

## Overview
This project is a deep dive into how buy and sell orders flow through the stock market and influence short-term price changes. I built a tool to analyse huge amounts of real-time order data (the “limit order book”), which shows every pending buy and sell order for a stock at any moment. By breaking down this data, I wanted to understand what drives prices to move within seconds or minutes and how traders and banks use this information to make faster, smarter decisions. The goal was to turn raw order-book data into clear insights that show how liquidity, supply and demand shape the market, while practising advanced data analysis and machine-learning techniques in a real-world finance context.

## Why I Chose This Project
I picked this project because it is far less common than traditional finance challenges. Watching the live flow of orders and seeing how that shapes price movement in real time was fascinating. I wanted to understand what happens behind the scenes, push myself on the engineering and data side and explore tools used by professional traders and quants.

## Problem Statement
My aim was to understand how limit-order-book dynamics can help predict very short-term price moves and to turn complex, high-frequency data into useful trading signals. I also wanted to build something that would stand out to future employers by combining technical engineering with practical financial insight.

## Business Context
Investment banks, hedge funds and high-frequency trading firms rely on the limit order book because it captures real-time supply and demand. By analysing how orders are placed, changed or cancelled, firms can predict short-term price moves, improve execution timing and manage market impact. Effective LOB modelling is therefore valuable for anyone targeting quantitative research, trading or financial-engineering roles.

## Data & Tools Used
- **Data**: High-frequency snapshots from the LOBSTER sample set for several FTSE 100 stocks (2023-24).  
- **Processing**: Python, Pandas and NumPy; data stored in Parquet for speed.  
- **Visualisation**: Matplotlib and Seaborn.  
- **Modelling**: scikit-learn (logistic regression and random forest) with joblib for parallel processing.  
- **Environment**: Jupyter Notebook for transparent, reproducible analysis.

## Methodology
I synchronised each order-book update to a uniform 100 ms grid to create a clean, time-aligned view of each stock’s buy and sell queues. From every snapshot I extracted trading features such as bid-ask spread, mid-price, top-five-level order imbalance and total depth on both sides of the book. Using these features, I built two prediction models—a logistic-regression baseline and a random-forest classifier—targeting the direction of the next one-second mid-price move. A walk-forward validation schedule (train on one day, test on the next) mimicked live trading and avoided look-ahead bias. Performance was tracked with accuracy and precision scores, and I visualised results with confusion-matrix heat maps to identify strengths and weaknesses.

## Results
Over the three-year test window the strategy generated a total profit of **£566** with a Sharpe ratio of **0.33**. The largest peak-to-trough decline (max drawdown) was about **£7,158**, and the equity curve shows that profits spent long periods between **£0** and **–£2,000** before recovering near the end. The model can occasionally capture profitable mean-reversion moves, but its signals are still noisy and the risk is too high for production use. A desk quant could use these findings as a starting point—refining entry and exit rules or adding tighter risk controls—to turn a patchy edge into a more consistent strategy.

## Key Challenges & Solutions
The hardest part was staying focused during heavy coding sessions. Diving straight into complex Python loops often made me lose sight of the objective and introduce small bugs. I solved this by breaking tasks into bite-sized steps, writing a short checklist for each session, adding frequent commits and documenting each code block clearly. This approach kept me oriented, sped up debugging and reduced errors.

## Takeaways
- Improved skills in writing and troubleshooting complex Python, especially for high-frequency data.  
- Learned to visualise order-book features and model results clearly.  
- Became more confident translating raw data into business insights.  
- Used AI tools (about 30 % of the final code) to overcome roadblocks and learn faster.  
- Gained practical understanding of how order-flow analytics can support better execution and risk management.

## Improvements
Next, I plan to rewrite the entire project without AI assistance to deepen my technical understanding. I also want to test the models on different asset classes and incorporate real-time data feeds to make the analysis more robust and realistic.

 


