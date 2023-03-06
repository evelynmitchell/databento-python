import asyncio

from databento import Historical


async def example_download_batch_job_async() -> None:
    key = "YOUR_API_KEY"
    client = Historical(key=key)

    # Will download all job files to a `my_data/YOUR_JOB_ID/` directory
    await client.batch.download_async(
        output_dir="my_data",
        job_id="YOUR_JOB_ID",  # <-- Discover this from `.list_jobs(...)`
    )


if __name__ == "__main__":
    asyncio.run(example_download_batch_job_async())
