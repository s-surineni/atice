var checkIfPrerequisite = function(numCourses, prerequisites, queries) {
    // initialize adjacency list
    let adjList = new Array(numCourses).fill().map(() => new Set());
    // initialize inDegree array
    const inDegree = new Array(numCourses).fill(0);
    for (let i = 0; i < prerequisites.length; i++) {
        const [prereq, course] = prerequisites[i];
        adjList[prereq].add(course);
        inDegree[course]++;
    }

    // topological sort
    const queue = [];
    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) {
            queue.push(i);
        }
    }
    // initialize result array with empty sets
    const preReqSet = new Array(numCourses).fill().map(() => new Set());
    while (queue.length > 0) {
        const course = queue.shift();
        for (const prereq of adjList[course]) {
            inDegree[prereq]--;
            preReqSet[prereq].add(course);
            // add all preReqSet[course] to preReqSet[prereq]
            for (const pre of preReqSet[course]) {
                preReqSet[prereq].add(pre);
            }
            if (inDegree[prereq] === 0) {
                queue.push(prereq);
            }
        }
    }
    // iterate over queries
    const res = [];
    for (const [prereq, course] of queries) {
        res.push(preReqSet[course].has(prereq));
    }
    return res;
};