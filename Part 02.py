# High achievers report & Bonus Task
# Part 02 & Part 03

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'university'
}


def get_high_achievers():
    """
    Get high achievers using SQL with GROUP BY and HAVING
    """
    connection = mysql.connector.connect(**DB_CONFIG)

    query = """
        SELECT 
            s.name AS student_name,
            ROUND(AVG(m.score), 2) AS average_score,
            CASE 
                WHEN AVG(m.score) > 85 THEN 'Distinction'
                WHEN AVG(m.score) >= 75 THEN 'Honours'
                ELSE 'Not Achieved'
            END AS final_grade
        FROM students s
        JOIN marks m ON s.student_id = m.student_id
        GROUP BY s.student_id, s.name
        HAVING AVG(m.score) > 75
        ORDER BY average_score DESC
    """

    df = pd.read_sql(query, connection)
    connection.close()
    return df


def get_all_averages():
    """
    Get all students' average scores for histogram
    """
    connection = mysql.connector.connect(**DB_CONFIG)

    query = """
        SELECT 
            s.name AS student_name,
            ROUND(AVG(m.score), 2) AS average_score
        FROM students s
        JOIN marks m ON s.student_id = m.student_id
        GROUP BY s.student_id, s.name
    """

    df = pd.read_sql(query, connection)
    connection.close()
    return df


def print_report(df):
    """Print report to console"""
    print("\n" + "=" * 60)
    print("HIGH ACHIEVERS REPORT")
    print("=" * 60)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Criteria: Average score > 75")
    print(f"Total students: {len(df)}")
    print("-" * 60)
    print(f"{'Student Name':<25} {'Avg Score':<12} {'Grade':<12}")
    print("-" * 60)

    for _, row in df.iterrows():
        print(f"{row['student_name']:<25} {row['average_score']:<12} {row['final_grade']:<12}")

    print("-" * 60)


def export_to_csv(df):
    """Export report to CSV"""
    filename = f"high_achievers_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False)
    print(f"\n✓ Exported to: {filename}")
    return filename


def create_histogram(df_all):
    """Create histogram of average scores"""
    plt.figure(figsize=(10, 6))

    # Create histogram
    sns.histplot(data=df_all, x='average_score', bins=15, color='skyblue', edgecolor='black')

    # Add threshold lines
    plt.axvline(x=75, color='orange', linestyle='--', linewidth=2, label='Honours Threshold (75)')
    plt.axvline(x=85, color='green', linestyle='--', linewidth=2, label='Distinction Threshold (85)')

    # Labels and title
    plt.title('Distribution of Student Average Scores', fontsize=14, fontweight='bold')
    plt.xlabel('Average Score', fontsize=12)
    plt.ylabel('Number of Students', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Save and show
    filename = f"score_distribution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(filename, dpi=100, bbox_inches='tight')
    print(f"✓ Histogram saved to: {filename}")
    plt.show()


def main():
    """Generate High Achievers Report"""
    print("=" * 60)
    print("PART 2: HIGH ACHIEVERS REPORT")
    print("=" * 60)

    # Get high achievers using SQL (GROUP BY + HAVING)
    df_high_achievers = get_high_achievers()

    # Print to console
    print_report(df_high_achievers)

    # Export to CSV
    export_to_csv(df_high_achievers)

    # Create histogram
    df_all = get_all_averages()
    create_histogram(df_all)

    print("\n✓ PART 2 COMPLETE!")


if __name__ == "__main__":
    main()