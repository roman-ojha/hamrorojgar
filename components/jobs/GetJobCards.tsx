import React, { useEffect } from "react";
import JobCard from "../JobCard";
import { useAppState } from "@/hooks/useAppState";
import { jobsSelector, JobState } from "@/store/selector";

const GetJobCards = (): React.JSX.Element => {
  const [{ fetchJobs, fetchJob }, [jobs]] = useAppState<[JobState[]]>([
    jobsSelector,
  ]);

  useEffect(() => {
    fetchJobs();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    if (jobs.length > 0) {
      fetchJob(jobs[0].id);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [jobs]);
  return (
    <>
      {jobs.map((job) => (
        <JobCard
          key={job.id}
          title={job.title}
          salary_from={job.salary_from}
          salary_to={job.salary_to}
          job_type={job.job_type}
          qualifications={job.qualifications}
        />
      ))}
    </>
  );
};

export default GetJobCards;