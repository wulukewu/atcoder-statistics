export async function fetchAtCoderData() {
  try {
    const response = await fetch('/api/data');
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching AtCoder data:', error);
    throw error;
  }
}
