import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import simulator as sm

df = pd.DataFrame(sm.all_calculations, columns=["Required_Score"])

sns.histplot(df, x="Required_Score", kde="True", bins=50)

plt.axvline(x=8.0, color='red', linestyle='--', label='Historical Average')

plt.savefig("carlsen_elo_distribution.png", dpi=300)

